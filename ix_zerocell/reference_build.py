"""Sizing and consistency checks for the concrete ZC-D10 assembly.

Values here check the declared design, not the identity/quality of purchased
parts and not the safe operation of a physical unit.
"""
import math
from .validation import number, positive


def backup_voltage(top_ohm=715000, bottom_ohm=162000, reference_v=1.2):
    positive(top_ohm,"top_ohm");positive(bottom_ohm,"bottom_ohm")
    positive(reference_v,"reference_v")
    return reference_v*(1+top_ohm/bottom_ohm)


def source_cutoff(top_ohm=2200, bottom_ohm=191, internal_pullup_ohm=100000):
    for value,name in [(top_ohm,"top_ohm"),(bottom_ohm,"bottom_ohm"),
                       (internal_pullup_ohm,"internal_pullup_ohm")]: positive(value,name)
    equivalent=top_ohm*internal_pullup_ohm/(top_ohm+internal_pullup_ohm)
    factor=1+equivalent/bottom_ohm
    return {"rising_v_typical":1.35*factor,"falling_v_typical":1.20*factor}


def minimum_nominal_capacitance(load_w, seconds, high_v, low_v,
                                output_efficiency=.85, internal_w=.05,
                                minimum_capacity_fraction=.63, leakage_a=0):
    """Dark-interval screen with conservative constant parasitic-power bounds.

    Leakage uses I_leak * V_high for the whole interval. Nominal capacitance
    accounts for both initial tolerance and aging via a caller-declared lower
    fraction. This says nothing about ESR, peak current or converter dropout.
    """
    for value,name in [(load_w,"load_w"),(seconds,"seconds"),(internal_w,"internal_w"),
                       (low_v,"low_v"),(leakage_a,"leakage_a")]: number(value,name)
    positive(high_v,"high_v")
    positive(output_efficiency,"output_efficiency")
    positive(minimum_capacity_fraction,"minimum_capacity_fraction")
    if low_v>=high_v or output_efficiency>1 or minimum_capacity_fraction>1:
        raise ValueError("invalid voltage/efficiency/capacity range")
    demand_j=seconds*(load_w/output_efficiency+internal_w+leakage_a*high_v)
    return 2*demand_j/((high_v**2-low_v**2)*minimum_capacity_fraction)


def series_assembly_for_dark_interval(load_w, hours, cell_f, series=4,
                                     high_v=10, low_v=4):
    positive(cell_f,"cell_f");number(hours,"hours")
    if type(series) is not int or series<1: raise ValueError("positive integer series count required")
    required=minimum_nominal_capacitance(load_w,hours*3600,high_v,low_v)
    one_string_f=cell_f/series
    strings=math.ceil(required/one_string_f)
    return {"required_nominal_bank_f":required,"parallel_strings":strings,
            "total_cells":strings*series,"origin":"sizing_assumptions",
            "assembly_released":False}


def design_report():
    return {"build_id":"ZC-D10","version":"0.2.0","hardware_measured":False,
            "stock_capacitor_count":4,"cell_f_nominal":10,
            "bank_f_nominal":2.5,"bank_float_v":10,
            "bank_total_energy_j":125,
            "bank_ideal_usable_j_10_to_3V":113.75,
            "backup_after_R3_change_v":backup_voltage(),
            "source_voltage_window":source_cutoff(),
            "bleed_ideal_seconds_10_to_0_5V":2.5*100*math.log(20),
            "base_continuous_target_w":10,"conditional_qualification_target_w":20,
            "source_input_limit_a":2,
            "source_12V_2A_gross_w":24,
            "illustrative_20W_input_w_at_90pct_final_and_98pct_pass":20/(.90*.98)+.05,
            "overnight_10W_16h_screen":series_assembly_for_dark_interval(10,16,10),
            "72h_10W_no_input_screen":series_assembly_for_dark_interval(10,72,10),
            "large_bank_screen_is_not_a_released_expansion_build":True}
