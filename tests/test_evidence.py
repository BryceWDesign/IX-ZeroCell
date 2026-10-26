import csv
import json
import tempfile
import unittest
from pathlib import Path

from ix_zerocell.evidence import digest, review
from ix_zerocell.validation import load_json


class EvidenceReview(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory()
        self.root=Path(self.temp.name)
        (self.root/"calibration.txt").write_text("SYNTHETIC TEST FIXTURE, not calibration evidence")
        (self.root/"protocol.txt").write_text("SYNTHETIC TEST FIXTURE, constant source/load")
        self.csv=self.root/"samples.csv"
        with self.csv.open("w",newline="") as f:
            writer=csv.writer(f)
            writer.writerow(["time_s","input_w","output_w","auxiliary_w","bank_v","output_v"])
            writer.writerows([[t,2,1.1,.1,5,5] for t in range(11)])
        self.meta={"schema":"1","origin":"synthetic",
                   "instrument_ids":{"input":"fixture-input","output":"fixture-output","storage":"fixture-storage"},
                   "artifacts":{},"capacitance_f":10,"capacitance_relative_error":.01,
                   "voltage_absolute_error_v":.001,"power_relative_error":.01,
                   "power_absolute_error_w":.001,"max_sample_gap_s":1,
                   "target_load_w":1,"minimum_duration_s":10,
                   "output_voltage_min_v":4.75,"output_voltage_max_v":5.25,
                   "max_unmetered_loss_w":1}
        self.bundle=self.root/"experiment.json"
        self.save()

    def tearDown(self): self.temp.cleanup()

    def save(self):
        for name, filename in [("samples","samples.csv"),("calibration","calibration.txt"),("protocol","protocol.txt")]:
            self.meta["artifacts"][name]={"path":filename,"sha256":digest(self.root/filename)}
        self.bundle.write_text(json.dumps(self.meta))

    def test_synthetic_never_qualifies_as_measurement_candidate(self):
        r=review(self.bundle)
        self.assertEqual(r["verdict"],"NOT_VALIDATED")
        self.assertFalse(r["hardware_validated"])

    def test_constant_power_trapezoidal_integral(self):
        r=review(self.bundle)
        self.assertAlmostEqual(r["input_j"],20)
        self.assertAlmostEqual(r["output_j"],11)
        self.assertAlmostEqual(r["unmetered_residual_j"],8)

    def test_measured_label_requires_review_and_never_proves_hardware(self):
        self.meta["origin"]="measured";self.save()
        r=review(self.bundle)
        self.assertEqual(r["verdict"],"MEASUREMENT_REVIEW_CANDIDATE")
        self.assertFalse(r["hardware_validated"])
        self.assertTrue(r["independent_review_required"])
        self.assertFalse(r["hashes_authenticate_measurements"])

    def test_output_energy_without_input_or_storage_fails(self):
        self.csv.write_text(self.csv.read_text().replace(",2,1.1,",",0,1.1,"))
        self.meta["origin"]="measured";self.save()
        self.assertFalse(review(self.bundle)["checks"]["energy_closure_within_declared_bounds"])

    def test_tampered_bytes_rejected(self):
        self.csv.write_text(self.csv.read_text()+"\n")
        with self.assertRaises(ValueError): review(self.bundle)

    def test_path_escape_rejected(self):
        self.meta["artifacts"]["samples"]["path"]="../outside.csv"
        self.bundle.write_text(json.dumps(self.meta))
        with self.assertRaises(ValueError): review(self.bundle)

    def test_time_reversal_rejected(self):
        text=self.csv.read_text();self.csv.write_text(text.replace("10,2,","8,2,"));self.save()
        with self.assertRaises(ValueError): review(self.bundle)

    def test_gap_rejected(self):
        self.meta["max_sample_gap_s"]=.5;self.save()
        with self.assertRaises(ValueError): review(self.bundle)

    def test_power_floor_includes_instrument_uncertainty(self):
        self.meta["power_relative_error"]=.2;self.save()
        self.assertFalse(review(self.bundle)["checks"]["load_power_at_sample_points"])

    def test_short_test_not_sustained_power_proof(self):
        self.meta["minimum_duration_s"]=20;self.save()
        self.assertFalse(review(self.bundle)["checks"]["sufficient_duration"])

    def test_duplicate_json_keys_rejected(self):
        self.bundle.write_text('{"origin":"measured","origin":"synthetic"}')
        with self.assertRaises(ValueError): load_json(self.bundle)

    def test_nan_json_rejected(self):
        self.bundle.write_text('{"power":NaN}')
        with self.assertRaises(ValueError): load_json(self.bundle)

    def test_ragged_csv_rejected(self):
        self.csv.write_text(self.csv.read_text()+"11,2\n");self.save()
        with self.assertRaises(ValueError): review(self.bundle)


if __name__ == "__main__": unittest.main()
