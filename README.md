# Python Loan Calculator

## Overview
CLI loan/mortgage helper that computes monthly payments, total interest, and schedules (annuity & differentiated). Hyperskill project.

## Tech
- Python 3.11+
- argparse
- math

## How to run

```bash
python -m venv .venv
source .venv/bin/activate
python main.py --principal 100000 --interest 7.8 --months 120
# or
python main.py --type annuity --principal 350000 --interest 3.2 --payment 1600
```

## Output
- Monthly payment or number of months
- Overpayment/total interest
- (Optional) per-month schedule
