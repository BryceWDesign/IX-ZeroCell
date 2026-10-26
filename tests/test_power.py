import math
import random
import unittest

from ix_zerocell.power import Bank, Bus, Source
from ix_zerocell.sources import (pv_power, kinetic_power, teg_power, rf_power,
                                recirculating_net_power, thermal_temperature)
from ix_zerocell.experiments import campaign, run_scenario


class BankPhysics(unittest.TestCase):
    def test_three_series_cells_capacitance_and_energy(self):
        b = Bank(series=3, cell_f=1000, cell_max_v=2.7, cutoff_v=5.5)
        self.assertAlmostEqual(b.capacitance_f, 1000 / 3)
        self.assertAlmostEqual(b.usable_wh, 1.637037037037037)
        self.assertAlmostEqual(b.energy_j(8.1), 10935)

    def test_parallel_cells_preserve_energy(self):
        b = Bank(series=3, parallel=4, cell_f=1000, cell_max_v=2.7)
        self.assertAlmostEqual(b.energy_j(b.max_v), 12 * .5 * 1000 * 2.7 ** 2)

    def test_invalid_bank_inputs(self):
        for params in [dict(series=True), dict(series=1.5), dict(parallel=0),
                       dict(cell_f=math.nan), dict(leakage_bank_a=-1),
                       dict(cutoff_v=11), dict(max_discharge_a=math.inf)]:
            with self.subTest(params=params), self.assertRaises(ValueError): Bank(**params)

    def test_zero_input_empty_bank_delivers_nothing(self):
        bus = Bus()
        for _ in range(50):
            r = bus.step([], 5, 1, .01)
            self.assertEqual(r.output_j, 0)
            self.assertEqual(r.residual_j, 0)

    def test_exact_constant_current_charge(self):
        b = Bank(series=1, cell_f=10, cell_max_v=5, cutoff_v=0,
                 cell_dc_resistance_ohm=0, leakage_bank_a=0, max_charge_a=1)
        bus = Bus(b, initial_v=0, charge_efficiency=1, output_efficiency=1)
        bus.step([Source("supply", 100, 1, 100)], 0, 10)
        self.assertAlmostEqual(bus.voltage, 1)
        self.assertAlmostEqual(bus.energy, 5)

    def test_exact_discharge_and_resistive_heat(self):
        b = Bank(series=1, cell_f=10, cell_max_v=5, cutoff_v=0,
                 cell_dc_resistance_ohm=.1, leakage_bank_a=0, max_discharge_a=1)
        bus = Bus(b, initial_v=5, output_efficiency=1, output_limit_w=100)
        r = bus.step([], 100, 10)
        self.assertAlmostEqual(bus.voltage, 4)
        self.assertAlmostEqual(r.capacitor_resistance_loss_j, 1)
        self.assertAlmostEqual(r.output_j, 44)
        self.assertAlmostEqual(r.residual_j, 0)

    def test_direct_source_avoids_charge_discharge_penalty(self):
        bus = Bus(initial_v=0, output_efficiency=.8)
        r = bus.step([Source("input", 2, .5, 10)], .8, 1)
        self.assertAlmostEqual(r.output_j, .8)
        self.assertAlmostEqual(r.output_loss_j, .2)
        self.assertAlmostEqual(r.storage_change_j, 0)

    def test_output_ceiling_and_unmet_load(self):
        r = Bus(initial_v=10, output_limit_w=1).step([], 10, 1)
        self.assertAlmostEqual(r.output_j, 1)
        self.assertAlmostEqual(r.unmet_output_j, 9)

    def test_charge_full_bank_spills_surplus(self):
        b = Bank(leakage_bank_a=0)
        r = Bus(b, 10).step([Source("solar", 20, .8, 20)], 0, 10)
        self.assertAlmostEqual(r.curtailed_j, 160)
        self.assertEqual(r.storage_change_j, 0)

    def test_no_free_energy_through_closed_feedback_loop(self):
        self.assertLess(recirculating_net_power(10, .8), 0)
        self.assertEqual(recirculating_net_power(10, 1), 0)

    def test_rf_minus20dbm_is_ten_microwatts_before_rectification(self):
        self.assertAlmostEqual(rf_power(-20, 1), 10e-6)

    def test_kinetic_budget_cannot_be_multiplied_by_coil_count(self):
        self.assertAlmostEqual(kinetic_power(.1, 2, 1, .5), .1)

    def test_temperature_difference_needs_real_heat_flow(self):
        self.assertEqual(teg_power(1, 1, 400, 300, 0), 0)
        self.assertEqual(teg_power(2, 1, 400, 300, 1), .25)
        self.assertEqual(teg_power(0, 1, 300, 300, 1), 0)
        with self.assertRaises(ValueError): teg_power(1, 1, 300, 300, 1)

    def test_thermal_model_matches_time_constant(self):
        self.assertAlmostEqual(thermal_temperature(25,25,2,10,100,1000),
                               45 - 20 / math.e)

    def test_source_physical_ranges(self):
        self.assertEqual(pv_power(20,0),0)
        self.assertEqual(pv_power(20,1000,.8),16)
        for call in [lambda: pv_power(1,1,2), lambda: rf_power(math.nan,.5),
                     lambda: kinetic_power(1,1,-1), lambda: teg_power(1,0,400,300,1),
                     lambda: recirculating_net_power(1,1.01)]:
            with self.assertRaises(ValueError): call()

    def test_reject_nan_infinity_boolean_negative_and_zero_dt(self):
        for bad in [math.nan, math.inf, True, -1]:
            with self.assertRaises(ValueError): Bus().step([],bad,1)
        with self.assertRaises(ValueError): Bus().step([],1,0)
        with self.assertRaises(ValueError): Bus(output_efficiency=1.1)

    def test_no_duplicate_metered_source(self):
        sources = [Source("same",1,.8,1), Source("same",1,.8,1)]
        with self.assertRaises(ValueError): Bus().step(sources,0,1)

    def test_randomized_energy_closure_and_limits(self):
        rng = random.Random(62931)
        for _ in range(400):
            bank = Bank(series=rng.randint(1,4), cell_f=rng.uniform(1,3000),
                        cutoff_v=0, cell_dc_resistance_ohm=rng.uniform(0,.1),
                        leakage_bank_a=rng.uniform(0,.01),
                        max_charge_a=rng.uniform(.01,3), max_discharge_a=rng.uniform(.01,3))
            bus = Bus(bank, rng.uniform(0,bank.max_v),
                      charge_efficiency=rng.uniform(.1,1), output_efficiency=rng.uniform(.1,1))
            for _ in range(10):
                r = bus.step([Source("external",rng.uniform(0,20),rng.uniform(0,1),10)],
                             rng.uniform(0,20),rng.uniform(.01,10),.01)
                self.assertLess(abs(r.residual_j),1e-7)
                self.assertGreaterEqual(bus.energy,0)
                self.assertLessEqual(bus.voltage,bank.max_v+1e-10)
                self.assertGreaterEqual(r.output_j,0)

    def test_analytical_no_loss_runtime(self):
        b = Bank(series=1,cell_f=10,cell_max_v=5,cutoff_v=3,
                 cell_dc_resistance_ohm=0,leakage_bank_a=0,max_discharge_a=10)
        bus = Bus(b,5,output_efficiency=1,output_limit_w=100)
        delivered=sum(bus.step([],1,1).output_j for _ in range(100))
        self.assertAlmostEqual(delivered,.5*10*(25-9))


class Scenarios(unittest.TestCase):
    @classmethod
    def setUpClass(cls): cls.report=campaign()

    def test_hardware_claim_never_derived_from_simulation(self):
        self.assertFalse(self.report["hardware_validated"])
        self.assertTrue(all(not s["hardware_validated"] for s in self.report["scenarios"]))

    def test_negative_controls_fail_and_real_inputs_deliver_in_model(self):
        cases={s["name"]:s for s in self.report["scenarios"]}
        for name in ["RF_only_large_bank_negative_control", "no_input_empty_bank_negative_control",
                     "large_bank_5W_generator_10min_cold_start_negative_control"]:
            self.assertEqual(cases[name]["output_wh"],0)
        self.assertGreater(cases["20W_panel_daylight_1W_light"]["output_wh"],0)
        self.assertGreater(cases["starter_bank_5W_generator_10min_then_1W_light"]["output_wh"],0)
        self.assertGreater(cases["microharvester_small_bank_sensor"]["output_wh"],0)

    def test_dark_output_cannot_exceed_initial_usable_energy(self):
        s=next(s for s in self.report["scenarios"] if s["name"]=="charged_field_bank_dark_5W_USB")
        self.assertLess(s["output_wh"],Bank().usable_wh*.88)

    def test_direct_path_avoids_waiting_for_large_storage(self):
        cases={s["name"]:s for s in self.report["scenarios"]}
        direct=cases["20W_panel_priority_direct_path_1W_light"]
        waiting=cases["20W_panel_daylight_1W_light"]
        self.assertEqual(direct["first_99_percent_load_s"],5)
        self.assertLess(direct["first_99_percent_load_s"],waiting["first_99_percent_load_s"])
        self.assertGreater(direct["output_wh"],waiting["output_wh"])

    def test_20W_extension_requires_input_and_stops_when_storage_runs_out(self):
        cases={s["name"]:s for s in self.report["scenarios"]}
        sunny=cases["50W_panel_priority_direct_path_20W_DC"]
        interrupted=cases["20W_DC_solar_loss_after_one_hour"]
        self.assertEqual(sunny["seconds_at_99_percent_load"],7195)
        self.assertGreater(interrupted["requested_but_not_served_wh"],0)
        self.assertLess(interrupted["seconds_at_99_percent_load"],7200)

    def test_step_halving_agrees_on_energy(self):
        bank=Bank(leakage_bank_a=0)
        outputs=[]
        for step in [1,.5]:
            outputs.append(run_scenario("comparison",bank,lambda t: [],1,1000,
                                        initial_v=9,start_v=8,step_s=step)["output_wh"])
        self.assertLess(abs(outputs[0]-outputs[1]),1e-5)

    def test_invalid_scenario_timing(self):
        for step in [math.nan,0,math.inf,1e-12]:
            with self.assertRaises(ValueError): campaign(step)


if __name__ == "__main__": unittest.main()
