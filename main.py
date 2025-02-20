import math
import argparse


def calculate_annuity_payment(principal, periods, interest):
    i = interest / (12 * 100)
    annuity_payment = principal * i * (1 + i)**periods / ((1 + i)**periods - 1)
    return math.ceil(annuity_payment)


def calculate_number_of_periods(principal, payment, interest):
    i = interest / (12 * 100)
    n = math.log(payment / (payment - i * principal), 1 + i)
    return math.ceil(n)


def calculate_loan_principal(payment, periods, interest):
    i = interest / (12 * 100)
    principal = payment / (i * (1 + i)**periods / ((1 + i)**periods - 1))
    return math.floor(principal)


def calculate_differentiated_payments(principal, periods, interest):
    i = interest / (12 * 100)
    total_payment = 0
    for month in range(1, periods + 1):
        dm = math.ceil(principal / periods + i * (principal - (principal * (month - 1)) / periods))
        total_payment += dm
        print(f"Month {month}: payment is {dm}")
    overpayment = total_payment - principal
    print(f"Overpayment = {overpayment}")


def display_months_as_years_and_months(months):
    years = months // 12
    months = months % 12
    if years == 0:
        return f"{months} months"
    elif months == 0:
        return f"{years} years"
    else:
        return f"{years} years and {months} months"


# Set up argparse
parser = argparse.ArgumentParser(description="Loan Calculator")
parser.add_argument("--type", help="Type of payment: 'annuity' or 'diff'")
parser.add_argument("--principal", type=float, help="Loan principal")
parser.add_argument("--payment", type=float, help="Monthly payment")
parser.add_argument("--periods", type=int, help="Number of months")
parser.add_argument("--interest", type=float, help="Annual interest rate (as a percentage, not a decimal)")
args = parser.parse_args()

# Validate required arguments
if (args.type not in ["annuity", "diff"] or not args.interest or args.interest <= 0 or
    (args.principal is not None and args.principal < 0) or
    (args.payment is not None and args.payment < 0) or
    (args.periods is not None and args.periods < 0)):
    print("Incorrect parameters")
elif args.type == "diff" and args.payment:
    print("Incorrect parameters")
elif args.principal and args.periods and args.interest and args.type == "diff":
    # Calculate differentiated payments
    calculate_differentiated_payments(args.principal, args.periods, args.interest)
elif args.type == "annuity":
    if args.principal and args.payment and args.interest and not args.periods:
        # Calculate the number of periods
        periods = calculate_number_of_periods(args.principal, args.payment, args.interest)
        time = display_months_as_years_and_months(periods)
        print(f"It will take {time} to repay this loan!")
        overpayment = args.payment * periods - args.principal
        print(f"Overpayment = {overpayment}")
    elif args.principal and args.periods and args.interest and not args.payment:
        # Calculate the annuity payment
        payment = calculate_annuity_payment(args.principal, args.periods, args.interest)
        print(f"Your monthly payment = {payment}!")
        overpayment = payment * args.periods - args.principal
        print(f"Overpayment = {overpayment}")
    elif args.payment and args.periods and args.interest and not args.principal:
        # Calculate the loan principal
        principal = calculate_loan_principal(args.payment, args.periods, args.interest)
        print(f"Your loan principal = {principal}!")
        overpayment = args.payment * args.periods - principal
        print(f"Overpayment = {overpayment}")
    else:
        print("Incorrect parameters")
else:
    print("Incorrect parameters")
