"""Strict public input validation. No silently accepted NaN or duplicate JSON keys."""

import json
import math
from pathlib import Path


def number(value, name, minimum=0.0, maximum=math.inf):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{name}: finite number required")
    if not math.isfinite(value) or not minimum <= value <= maximum:
        raise ValueError(f"{name}: outside [{minimum}, {maximum}]")
    return float(value)


def positive(value, name):
    x = number(value, name)
    if x == 0:
        raise ValueError(f"{name}: must be positive")
    return x


def integer(value, name, minimum=1):
    if type(value) is not int or value < minimum:
        raise ValueError(f"{name}: integer >= {minimum} required")
    return value


def load_json(path):
    def constant(value):
        raise ValueError(f"nonstandard JSON constant: {value}")

    def unique(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"duplicate JSON field: {key}")
            result[key] = value
        return result

    return json.loads(Path(path).read_text(encoding="utf-8"),
                      parse_constant=constant, object_pairs_hook=unique)
