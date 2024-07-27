loan_principal = 'Loan principal: 1000'
final_output = 'The loan has been repaid!'
first_month = 'Month 1: repaid 250'
second_month = 'Month 2: repaid 250'
third_month = 'Month 3: repaid 500'


# write your code here
def calculate_number_of_payments_or_amount():

    import math

    print("Enter the loan principal: ")
    principal = float(input())  # loan principal

    print("What do you want to calculate?",
          "type 'm' for number of monthly payments,",
          "type 'p' for the monthly payment: ", sep='\n')

    user_answer = input()

    if user_answer == "m":
        print("Enter monthly payment: ")
        monthly_payment = float(input())

        number_months = principal / monthly_payment

        if round(number_months) != 1:
            print("It will take " + str(round(number_months)) + " months to repay the loan")
        else:
            print("It will take 1 month to repay the loan")

    if user_answer == "p":
        print("Enter the number of months: ")
        months = int(input())

        monthly_pay = principal / months

        last_pay = principal - (months - 1) * math.ceil(monthly_pay)

        if last_pay == 0:
            print("Your monthly payment = " + str(math.ceil(monthly_pay)))

        else:
            print("Your monthly payment = " + str(math.ceil(monthly_pay)),
                  " and the last payment = " + str(math.ceil(last_pay)))


# ------calculate annuity and differentiate payment

# calculate interest rate
def calculate_nominal_interest_rate(interest):
    i = interest / (12 * 100)
    return i


# calculate the number of payments
def calculate_number_of_monthly_payments(payment, interest, principal):

    import math

    i = calculate_nominal_interest_rate(interest)
    periods = math.log((payment / (payment - i * principal)), (1 + i))
    months = periods % 12
    months = math.ceil(months)
    periods = round(periods)
    years = periods // 12
    overpayment = payment * periods - principal
    if years != 1:
        if periods % 12 > 1:
            return (f"It will take {years} years and {months} months to repay this loan!"
                    f"\nOverpayment = {math.ceil(overpayment)}")
        elif periods % 12 == 1:
            return (f"It will take {years} years and one month to repay this loan!"
                    f"\nOverpayment = {math.ceil(overpayment)}")
        else:
            return (f"It will take {years} years to repay this loan!"
                    f"\nOverpayment = {math.ceil(overpayment)}")

    if years == 1:
        return ("It will take a year to repay this loan!"
                f"\nOverpayment = {math.ceil(overpayment)}")

    if years == 0 and periods != 1:
        return (f"It will take {periods} months to repay this loan!"
                f"\nOverpayment = {math.ceil(overpayment)}")
    elif years == 0 and periods == 1:
        return ("It will take a month to repay this loan!"
                f"\nOverpayment = {math.ceil(overpayment)}")

    if periods <= 0:
        return ("It will take less than a month to repay this loan!"
                f"\nOverpayment = {math.ceil(overpayment)}")

    return overpayment


# calculate annuity
def calculate_annuity(principal, interest, periods):

    import math

    i = calculate_nominal_interest_rate(interest)

    const = math.pow((1 + i), periods) 

    annuity_payment = principal * (i * const) / (const - 1)

    overpayment = math.ceil(annuity_payment) * periods - principal

    return (f"Your annuity payment = {math.ceil(annuity_payment)}!"
            f"\nOverpayment = {math.ceil(overpayment)}")


# calculate loan principal
def calculate_principal(payment, interest, periods):

    import math

    i = calculate_nominal_interest_rate(interest)

    const = math.pow((1 + i), periods)

    principal = payment / ((i * const) / (const - 1))

    overpayment = payment * periods - principal

    print(f"Your loan principal = {math.ceil(principal)}!"
          f"\nOverpayment = {math.ceil(overpayment)}")
# calculate_principal(payment=8722, interest=5.6, periods=120)


def calculate_differential(principal, periods, interest):

    import math

    i = calculate_nominal_interest_rate(interest)
    payments = []
    m = 1

    for month in range(1, periods + 1):

        month_payment = principal / periods + i * (principal - (principal * (month - 1)) / periods)

        payments.append(math.ceil(month_payment))

    for payment in payments:
        print(f"Month {m}: payment is {payment}")
        m += 1

    overpayment = sum(payments) - principal

    print(f"Overpayment = {math.ceil(overpayment)}")


def loan_calculator():

    import argparse
    import sys

    # parse provided parameters
    parser = argparse.ArgumentParser(description="Loan calculator for annuity payment")
    parser.add_argument("--principal", type=float, help="Total loan")
    parser.add_argument("--periods", type=int, help="The number of months to pay the loan")
    parser.add_argument("--interest", type=float, help="The annual interest rate")
    parser.add_argument("--payment", type=float, help="The fixed amount that is paid per defined time e.g. monthly")
    parser.add_argument("--type", type=str, help="The type of loan")  # choices=["diff", "annuity"]
    args = parser.parse_args()

    # check if number of arguments is correct
    arguments = sys.argv

    if len(arguments) < 4:  # min of 4 arguments must be provided for both options
        return print("Incorrect parameters")

    # if not diff or not annuity
    if args.type != "diff" and args.type != "annuity":
        return print("Incorrect parameters")

    if args.type == "diff":  # if diff then payment must be provided
        if args.payment is not None:
            return print("Incorrect parameters")

    if args.interest is None:  # interest must be provided
        return print("Incorrect parameters")

    # arguments must be positive
    if args.principal is not None:
        if args.principal < 0:
            return print("Incorrect parameters")

    if args.periods is not None:
        if args.periods < 0:
            return print("Incorrect parameters")

    if args.interest is not None:
        if args.interest < 0:
            return print("Incorrect parameters")

    if args.payment is not None:
        if args.payment < 0:
            return print("Incorrect parameters")

    # output based on the arguments provided
    if args.type == "diff":
        differential = calculate_differential(args.principal, args.periods, args.interest)
        return differential

    elif args.payment is None:
        payment = calculate_annuity(args.principal, args.interest, args.periods)
        return payment

    elif args.periods is None:
        periods = calculate_number_of_monthly_payments(args.payment, args.interest, args.principal)
        return periods

    elif args.principal is None:
        principal = calculate_principal(args.payment, args.interest, args.periods)
        return principal

    else:
        return "Incorrect parameters"


loan_calculator()
