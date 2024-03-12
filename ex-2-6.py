# ex-2-6.py
#    A program to compute the value of an investment
#    carried n years into the future


def main():
    print("This program calculates the future value")
    print("of years investment.")
    
    principal = eval(input("Enter the initial pricipal: "))
    apr = eval(input("Enter the annual interest rate: "))
    years = eval(input("Enter the number of years for the investment: "))

    for i in range(years):
        principal = principal * (1+apr)

    print("The value in 10 years is:", principal)

main()
