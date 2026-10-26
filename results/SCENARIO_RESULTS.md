# Simulated service and cold-start results

These are assumption-based computations, not measured ZeroCell performance.

| Scenario | First full-load time (s) | Full-load seconds | Useful output (Wh) |
|---|---:|---:|---:|
| 20W_panel_daylight_1W_light | 3297.0 | 3903.0 | 1.084167 |
| 20W_panel_priority_direct_path_1W_light | 5.0 | 7195.0 | 1.998611 |
| 50W_panel_priority_direct_path_20W_DC | 5.0 | 7195.0 | 39.972222 |
| 20W_DC_solar_loss_after_one_hour | 0.0 | 4912.0 | 27.291025 |
| charged_field_bank_dark_5W_USB | 0.0 | 5218.0 | 7.248212 |
| large_bank_5W_generator_10min_cold_start_negative_control | never | 0.0 | 0.000000 |
| starter_bank_5W_generator_10min_then_1W_light | 176.0 | 861.0 | 0.239405 |
| RF_only_large_bank_negative_control | never | 0.0 | 0.000000 |
| no_input_empty_bank_negative_control | never | 0.0 | 0.000000 |
| microharvester_small_bank_sensor | 1628.0 | 5572.0 | 0.000155 |

Full load means at least 99% of the requested power in a modeled step. The 5-second direct-source startup is an assumption. Full-load seconds include service while the input remains connected; they are not all post-source runtime.

The large empty bank/hand-generator case intentionally fails to start. The starter case charges a smaller separate bank. The model does not claim to implement or experimentally test the complete staged switching circuit.

## Sensitivity to unmeasured bank properties

Charged 10 V field bank, 5 W load, no external input; each case begins at its declared voltage and runs for two hours.

| Per-cell capacitance (F) | Bank leakage (mA) | Full-load minutes | Useful Wh |
|---:|---:|---:|---:|
| 2400 | 1.0 | 69.95 | 5.8295 |
| 2400 | 5.0 | 69.57 | 5.7986 |
| 2400 | 10.0 | 69.12 | 5.7604 |
| 3000 | 1.0 | 87.43 | 7.2868 |
| 3000 | 5.0 | 86.97 | 7.2482 |
| 3000 | 10.0 | 86.40 | 7.2005 |
| 3600 | 1.0 | 104.92 | 8.7442 |
| 3600 | 5.0 | 104.37 | 8.6979 |
| 3600 | 10.0 | 103.68 | 8.6406 |

This is a parameter sweep, not a statistical confidence interval. Actual capacitance, leakage, efficiency and operating temperature still require measurement.
