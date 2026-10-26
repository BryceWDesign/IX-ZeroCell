import argparse
import json
from pathlib import Path
from .experiments import campaign
from .evidence import review
from .reference_build import design_report
from .stack import StackDesign


def main():
    parser = argparse.ArgumentParser(description="IX-ZeroCell engineering and evidence tools")
    sub = parser.add_subparsers(dest="command", required=True)
    screen = sub.add_parser("campaign", help="run declared simulation scenarios")
    screen.add_argument("--out", type=Path)
    screen.add_argument("--step-s", type=float, default=1)
    evidence = sub.add_parser("review", help="review a local metered experiment bundle")
    evidence.add_argument("bundle", type=Path)
    sub.add_parser("reference", help="show the concrete ZC-D10 build calculations")
    sub.add_parser("stack", help="show revised twenty-channel 1 kW design calculations")
    args = parser.parse_args()
    try:
        if args.command == "campaign": result = campaign(args.step_s)
        elif args.command == "reference": result = design_report()
        elif args.command == "stack": result = StackDesign().bounds()
        else: result = review(args.bundle)
    except (ValueError, OSError, KeyError, TypeError) as exc:
        parser.exit(2, f"error: {exc}\n")
    rendered = json.dumps(result, indent=2, allow_nan=False) + "\n"
    if args.command == "campaign" and args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(rendered, encoding="utf-8")
        print(f"Saved {len(result['scenarios'])} simulated scenarios to {args.out}")
    else:
        print(rendered, end="")
    if args.command == "review" and result["verdict"] == "NOT_VALIDATED":
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
