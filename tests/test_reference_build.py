import json
import math
from pathlib import Path
import unittest
from ix_zerocell.reference_build import (backup_voltage,source_cutoff,
    minimum_nominal_capacitance,series_assembly_for_dark_interval,design_report)

ROOT=Path(__file__).resolve().parents[1]


class ConcreteBuild(unittest.TestCase):
    def test_backup_change_resolves_nominal_six_volt_headroom(self):
        self.assertAlmostEqual(backup_voltage(),6.496296296296297)
        self.assertGreater(backup_voltage(),6.3)
        self.assertLess(backup_voltage(649000),6.1)

    def test_uvlo_order_is_above_buck_dropout_and_below_panel_voc(self):
        window=source_cutoff()
        self.assertGreater(window['falling_v_typical'],13.3)
        self.assertGreater(window['rising_v_typical'],window['falling_v_typical'])
        self.assertLess(window['rising_v_typical'],23.3)

    def test_stock_bank_not_confused_with_thousands_of_farads(self):
        r=design_report()
        self.assertEqual(r['bank_f_nominal'],2.5)
        self.assertEqual(r['bank_total_energy_j'],125)
        self.assertLess(r['bank_ideal_usable_j_10_to_3V']/10,12)

    def test_overnight_is_a_real_storage_requirement(self):
        required=minimum_nominal_capacitance(10,16*3600,10,4)
        self.assertGreater(required,20000)
        self.assertGreater(required,2.5*1000)

    def test_72_hours_without_input_is_not_a_claim_of_stock_build(self):
        r=series_assembly_for_dark_interval(10,72,10)
        self.assertGreater(r['total_cells'],100000)
        self.assertFalse(r['assembly_released'])

    def test_parasitics_are_counted_even_when_useful_load_is_zero(self):
        self.assertGreater(minimum_nominal_capacitance(0,3600,10,4,internal_w=.05),0)
        self.assertGreater(minimum_nominal_capacitance(1,3600,10,4,leakage_a=.01),
                           minimum_nominal_capacitance(1,3600,10,4,leakage_a=0))

    def test_invalid_sizing_data_rejected(self):
        for kwargs in [dict(load_w=math.nan),dict(output_efficiency=0),
                       dict(minimum_capacity_fraction=1.1),dict(low_v=11)]:
            base=dict(load_w=1,seconds=100,high_v=10,low_v=4);base.update(kwargs)
            with self.assertRaises(ValueError): minimum_nominal_capacitance(**base)

    def test_every_route_terminates_on_a_real_declared_terminal(self):
        w=json.loads((ROOT/'hardware/reference_build/wiring.json').read_text())
        seen=set()
        for route in w['connections']:
            self.assertNotIn(route['wire'],seen);seen.add(route['wire'])
            for key in ['from','to']:
                component,terminal=route[key].split('.')
                self.assertIn(terminal,w['terminals'][component])
            self.assertLessEqual(route['awg'],24)
            self.assertGreater(route['maximum_route_mm'],0)

    def test_every_required_module_and_modification_is_in_BOM(self):
        b=json.loads((ROOT/'hardware/reference_build/BOM.json').read_text())
        p={x['ref']:x for x in b['parts']}
        self.assertEqual(p['U2']['part_or_purchase_spec'],'DC1937B')
        self.assertEqual(p['U1']['part_or_purchase_spec'],'D36V50F12 / item 4095')
        self.assertIn('715 kohm',p['RFB1']['part_or_purchase_spec'])
        self.assertIn('191 ohm',p['RUV2']['part_or_purchase_spec'])
        self.assertEqual(p['JC4-JC6']['quantity'],3)
        self.assertEqual(p['JC1-JC3']['quantity'],3)
        self.assertTrue(all(type(x['quantity']) is int and x['quantity']>0 for x in p.values()))
        self.assertFalse(b['hardware_measured'])

    def test_no_added_storage_requires_unreleased_large_bank_changes(self):
        b=json.loads((ROOT/'hardware/reference_build/BOM.json').read_text())
        self.assertTrue(b['do_not_buy_extra_bank_for_stock_build'])
        self.assertEqual(b['stock_U2_components_included']['capacitance_each_f'],10)


if __name__=='__main__': unittest.main()
