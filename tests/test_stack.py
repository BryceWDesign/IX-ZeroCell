import unittest, math
from dataclasses import replace
from ix_zerocell.stack import StackDesign,simulate,solve_combiner,rf_budget,static_budget
class StackCases(unittest.TestCase):
 def test_energy_is_sum_of_banks_not_square_of_count(self):
  d=StackDesign();r=d.bounds();self.assertAlmostEqual(r['usable_stack_kwh'],35.109)
  self.assertTrue(r['capacity_check']);self.assertTrue(r['daily_energy_check'])
 def test_previous_56_module_bank_not_silently_reused_for_higher_budget(self):
  r=replace(StackDesign(),modules_per_channel=56).bounds();self.assertLess(r['night_margin_wh'],.05*r['night_channel_wh'])
  r=StackDesign().bounds();self.assertGreater(r['night_margin_wh'],.05*r['night_channel_wh'])
 def test_no_input_empty_store_produces_no_output(self):
  r=simulate(StackDesign(channels=1),days=1,initial_v=0,continuous_dark=True)
  self.assertEqual(r['channel_output_j'],0);self.assertGreater(r['unserved_total_wh'],0)
 def test_conservation_under_source_loss(self):
  r=simulate(StackDesign(channels=1),days=1)
  self.assertLess(abs(r['closure_j']),.01);self.assertTrue(r['served_all_budgeted_load'])
 def test_zero_collecting_area_does_not_make_rf_power(self):
  self.assertEqual(rf_budget(100,0,1),0)
 def test_rf_units_and_auxiliaries(self):
  self.assertAlmostEqual(rf_budget(.01,100,.5,.1),.4)
 def test_static_needs_recharge(self):
  self.assertEqual(static_budget(1e-9,10000,0,0,.5),0)
  self.assertAlmostEqual(static_budget(1e-9,10000,0,10,.5),.25)
 def test_nonfinite_and_efficiency_errors(self):
  for f in [lambda:rf_budget(math.nan,1,1),lambda:static_budget(1,2,3,1,.5),lambda:StackDesign(output_efficiency=1.1),lambda:StackDesign(channels=0)]:
   with self.assertRaises(ValueError):f()
 def test_unsupported_source_power_is_rejected(self):
  with self.assertRaises(ValueError):StackDesign(pv_w=300)
 def test_combiner_power_and_channel_limit(self):
  r=solve_combiner([49.5]*20,[1.25]*20,[1.17]*20,1050)
  self.assertTrue(r['supplied']);self.assertAlmostEqual(r['output_w'],1050)
  self.assertLessEqual(max(r['channel_a']),1.17);self.assertGreater(r['bus_v'],46.5)
 def test_nineteen_low_limit_channels_do_not_guarantee_full_power(self):
  self.assertFalse(solve_combiner([49.4]*19,[1.27]*19,[1.14]*19,1050)['supplied'])
  self.assertTrue(solve_combiner([49.4]*19,[1.27]*19,[1.14]*19,1000)['supplied'])
 def test_unpowered_channel_cannot_sink_current(self):
  r=solve_combiner([0]+[49.5]*19,[1.25]*20,[1.17]*20,1000)
  self.assertTrue(r['supplied']);self.assertEqual(r['channel_a'][0],0)
 def test_invalid_vectors(self):
  with self.assertRaises(ValueError):solve_combiner([49],[1,2],[1],10)
 def test_simulation_never_sets_hardware_flag(self):
  self.assertFalse(StackDesign().bounds()['hardware_validated'])
if __name__=='__main__':unittest.main()
