import csv,json,unittest
from pathlib import Path
from ix_zerocell.stack import StackDesign
R=Path(__file__).resolve().parents[1]
class StackAssets(unittest.TestCase):
 def test_inventory_matches_energy_storage_and_converters(self):
  b=json.loads((R/'hardware/stack1000/BOM.json').read_text());p={x['ref']:x for x in b['parts']}
  self.assertEqual(p['C01-C60']['stack_quantity'],StackDesign().channels*StackDesign().modules_per_channel)
  self.assertEqual(p['A1-A4']['stack_quantity'],80);self.assertEqual(p['PV1-PV3']['stack_quantity'],60)
  self.assertFalse(b['procurement_released']);self.assertFalse(b['hardware_measured'])
 def test_wire_schedule_has_no_bypassed_module_resistor(self):
  with (R/'hardware/stack1000/WIRING.csv').open() as f:rows=list(csv.DictReader(f))
  self.assertEqual(len(rows),len({r['id'] for r in rows}))
  pairs={(r['from'],r['to']) for r in rows}
  for i in range(1,21):
   for j in range(1,61):
    base=f'CH{i:02}.'
    self.assertIn((base+f'C{j:02}.positive',base+f'FC{j:02}.in'),pairs)
    self.assertIn((base+f'RC{j:02}.out',base+'CB+'),pairs)
    self.assertNotIn((base+f'C{j:02}.positive',base+'CB+'),pairs)
 def test_unfinished_protection_is_not_hidden(self):
  r=json.loads((R/'hardware/stack1000/release_gates.json').read_text())
  self.assertFalse(r['construction_released']);self.assertEqual(len(r['gates']),7)
  self.assertTrue(all(g['status']=='open' for g in r['gates']))
 def test_no_fabricated_measurement_rows(self):
  self.assertEqual(len((R/'measurements/stack1000/samples-header.csv').read_text().splitlines()),1)
 def test_configuration_document_matches_executable_parameters(self):
  r=json.loads((R/'hardware/stack1000/design.json').read_text())
  self.assertEqual(r['configuration'],StackDesign().bounds()['configuration'])
if __name__=='__main__':unittest.main()
