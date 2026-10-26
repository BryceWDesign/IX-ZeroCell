# Changelog

## 0.2.0, expanded before publication, 26 October 2026

- Integrate ZC-S1000 revision B: twenty-channel, nominal 48 V, 1,000 W useful-output design target.
- Replace conceptual custom output converter/sharing PCB with a populated DC1924A modification and passive ballast/diode sharing circuit, pending low-input/thermal qualification.
- Revise storage from 56 to 60 modules per channel and energy stress allowance from 55 to 60 W; include independent-bank and inadequate-source calculations.
- Add assembly-scope BOM, explicit connection schedule, 53-step staged walkthrough, external-energy qualification, uncertainty-aware twenty-bank evidence review and open construction-release gates.
- Execute five stack energy scenarios, steady-state sharing cases and five ngspice output-port cases; include no-source, overload, shaded-channel and failed-channel controls.
- Add twenty-channel advisory fault/load policy with native tests; retain the small-build AVR monitor without pretending it controls the stack.
- Preserve ZC-D10 small reference build and historical donor/archive material. Remove the obsolete update.patch; provide full-tree replacement instructions.
- Keep version 0.2.0. No GitHub push, measured hardware rating or certification is claimed.

Earlier 0.2.0 work introduced explicit source/storage accounting, local evidence review, fault controls, CI, archived unsupported 2025 claims and the ZC-D10 reference assembly. Historical donor test logs are retained with their original scope; they are not new power-device tests.
