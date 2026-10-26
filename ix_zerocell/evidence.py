"""Local measurement review. A hash or operator label does not authenticate a bench test."""

import csv
import hashlib
from pathlib import Path
from .validation import load_json, number, positive


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def artifact(root, record):
    if not isinstance(record, dict) or set(record) != {"path", "sha256"}:
        raise ValueError("artifact requires path and sha256")
    name = record["path"]
    if not isinstance(name, str) or not name or Path(name).is_absolute():
        raise ValueError("artifact path must be relative")
    path = (root / name).resolve()
    if not path.is_relative_to(root.resolve()) or not path.is_file():
        raise ValueError("artifact missing or outside bundle")
    if digest(path) != record["sha256"]:
        raise ValueError("artifact hash mismatch")
    return path


def review(bundle):
    """Integrate separately metered input/output/auxiliaries and storage change.

    Samples are synchronised connector powers; trapezoidal integration assumes
    linear changes between samples. The declared maximum gap must resolve the
    actual load/source waveform. Unknown waveform bandwidth requires human review.
    Positive residual is unmetered dissipation; negative beyond uncertainty fails.
    """
    bundle = Path(bundle)
    meta = load_json(bundle)
    fields = {"schema", "origin", "instrument_ids", "artifacts", "capacitance_f",
              "capacitance_relative_error", "voltage_absolute_error_v",
              "power_relative_error", "power_absolute_error_w", "max_sample_gap_s",
              "target_load_w", "minimum_duration_s", "output_voltage_min_v",
              "output_voltage_max_v", "max_unmetered_loss_w"}
    if not isinstance(meta, dict) or set(meta) != fields:
        raise ValueError("measurement metadata fields do not match schema")
    if meta["schema"] != "1" or meta["origin"] not in ("measured", "synthetic"):
        raise ValueError("invalid schema/origin")
    ids = meta["instrument_ids"]
    if (not isinstance(ids, dict) or set(ids) != {"input", "output", "storage"}
            or any(not isinstance(x, str) or not x.strip() for x in ids.values())):
        raise ValueError("all metering boundaries require instrument identifiers")
    if not isinstance(meta["artifacts"], dict) or set(meta["artifacts"]) != {"samples", "calibration", "protocol"}:
        raise ValueError("samples, calibration and protocol artifacts required")
    paths = {k: artifact(bundle.parent, v) for k, v in meta["artifacts"].items()}
    for key in fields - {"schema", "origin", "instrument_ids", "artifacts"}:
        number(meta[key], key)
    for key in ("capacitance_f", "max_sample_gap_s", "target_load_w", "minimum_duration_s"):
        positive(meta[key], key)
    for key in ("capacitance_relative_error", "power_relative_error"):
        number(meta[key], key, 0, 1)
    if not 0 < meta["output_voltage_min_v"] < meta["output_voltage_max_v"]:
        raise ValueError("invalid output voltage acceptance range")
    columns = ["time_s", "input_w", "output_w", "auxiliary_w", "bank_v", "output_v"]
    with paths["samples"].open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames != columns:
            raise ValueError("measurement CSV columns do not match schema")
        rows = []
        for raw in reader:
            if None in raw or any(v is None for v in raw.values()):
                raise ValueError("ragged CSV row")
            rows.append({k: number(float(v), k) for k, v in raw.items()})
    if len(rows) < 2:
        raise ValueError("at least two measurement samples required")
    energy = {k: 0.0 for k in ("input_w", "output_w", "auxiliary_w")}
    for first, last in zip(rows, rows[1:]):
        dt = last["time_s"] - first["time_s"]
        if not 0 < dt <= meta["max_sample_gap_s"]:
            raise ValueError("nonmonotonic time or unresolved sample gap")
        for key in energy:
            energy[key] += (first[key] + last[key]) * 0.5 * dt
    elapsed = rows[-1]["time_s"] - rows[0]["time_s"]
    c = meta["capacitance_f"]
    vi, vf = rows[0]["bank_v"], rows[-1]["bank_v"]
    stored_change = 0.5 * c * (vf ** 2 - vi ** 2)
    residual = energy["input_w"] - energy["output_w"] - energy["auxiliary_w"] - stored_change
    ev = meta["voltage_absolute_error_v"]
    # Worst-case, fully correlated instrument errors; no unsupported confidence level.
    error = (sum(energy.values()) * meta["power_relative_error"]
             + 3 * meta["power_absolute_error_w"] * elapsed
             + abs(stored_change) * meta["capacitance_relative_error"]
             + c * (vi + vf) * ev + c * ev ** 2)
    output_floor = min(r["output_w"] * (1 - meta["power_relative_error"])
                       - meta["power_absolute_error_w"] for r in rows)
    checks = {
        "declared_measured_origin": meta["origin"] == "measured",
        "sufficient_duration": elapsed >= meta["minimum_duration_s"],
        "load_power_at_sample_points": output_floor >= meta["target_load_w"],
        "output_voltage_at_sample_points": all(
            meta["output_voltage_min_v"] <= r["output_v"] - ev and
            r["output_v"] + ev <= meta["output_voltage_max_v"] for r in rows),
        "energy_closure_within_declared_bounds": -error <= residual <=
            meta["max_unmetered_loss_w"] * elapsed + error,
    }
    return {
        "origin": meta["origin"], "elapsed_s": elapsed,
        "input_j": energy["input_w"], "output_j": energy["output_w"],
        "auxiliary_j": energy["auxiliary_w"], "storage_change_j": stored_change,
        "unmetered_residual_j": residual, "worst_case_error_bound_j": error,
        "checks": checks,
        "verdict": "MEASUREMENT_REVIEW_CANDIDATE" if all(checks.values()) else "NOT_VALIDATED",
        "hardware_validated": False, "independent_review_required": True,
        "hashes_authenticate_measurements": False,
        "between_sample_behavior_verified": False,
        "bundle_sha256": digest(bundle),
    }
