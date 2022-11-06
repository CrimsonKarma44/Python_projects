# Automatic loan payment calculator


def main():
    print("This is a monthly payment loan calculator ")
    print()

    principal = float(input("loan amount: "))
    apr = float(input("annual interest rate: "))
    yrs = int(input("years"))

    monthly_interest_rate = apr/1200
    amount_months = yrs*12
    monthly_payment = principal*monthly_interest_rate/(1-(1+monthly_interest_rate)**(-amount_months))

    print("The monthly payment for this loan is: {:.2f}".format(monthly_payment))
    # print("The monthly payment for this loan is: %.2f" % monthly_payment)

main()