import csv,json,tempfile,unittest
from pathlib import Path
from ix_zerocell.evidence import digest
from ix_zerocell.stack_evidence import COLUMNS,review_stack
class StackEvidence(unittest.TestCase):
 def setUp(self):
  self.tmp=tempfile.TemporaryDirectory();self.p=Path(self.tmp.name)
  with (self.p/'samples.csv').open('w',newline='') as f:
   w=csv.writer(f);w.writerow(COLUMNS)
   w.writerow([0,0,1020,0,48]+[45.6]*20);w.writerow([1,0,1020,0,48]+[45.59]*20)
  (self.p/'calibration.txt').write_text('Synthetic test fixture, not calibration evidence.')
  (self.p/'protocol.txt').write_text('Synthetic negative-control fixture.')
  self.m={'schema':'stack-1','origin':'synthetic','serial_numbers':[f'test{i}' for i in range(20)],
  'capacitance_f':[7968]*20,'capacitance_relative_error':.01,'voltage_error_v':.01,
  'power_relative_error':.01,'power_error_w':.1,'max_gap_s':1,'instrument_ids':['synthetic-meter'],
  'artifacts':{k:{'path':v,'sha256':digest(self.p/v)} for k,v in {'samples':'samples.csv','calibration':'calibration.txt','protocol':'protocol.txt'}.items()}}
 def tearDown(self):self.tmp.cleanup()
 def run_review(self):
  p=self.p/'bundle.json';p.write_text(json.dumps(self.m));return review_stack(p)
 def test_synthetic_never_hardware_pass(self):
  r=self.run_review();self.assertEqual(r['verdict'],'NOT_VALIDATED');self.assertFalse(r['hardware_validated'])
 def test_origin_label_alone_does_not_create_a_16_hour_run(self):
  self.m['origin']='measured';r=self.run_review();self.assertFalse(r['checks']['sixteen_hours'])
 def test_twenty_banks_must_not_be_replaced_by_one_average(self):
  self.m['capacitance_f']=[7968]
  with self.assertRaises(ValueError):self.run_review()
 def test_duplicate_channel_id_rejected(self):
  self.m['serial_numbers'][1]=self.m['serial_numbers'][0]
  with self.assertRaises(ValueError):self.run_review()
 def test_hash_tampering_rejected(self):
  (self.p/'samples.csv').write_text('changed')
  with self.assertRaises(ValueError):self.run_review()
 def test_external_artifact_path_rejected(self):
  self.m['artifacts']['samples']['path']='../outside.csv'
  with self.assertRaises(ValueError):self.run_review()
 def test_long_sample_gap_cannot_be_used_to_certify_transients(self):
  self.m['max_gap_s']=60
  with self.assertRaises(ValueError):self.run_review()
 def test_nan_uncertainty_rejected(self):
  self.m['power_relative_error']=float('nan')
  with self.assertRaises(ValueError):self.run_review()
if __name__=='__main__':unittest.main()
