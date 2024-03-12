# ex-2-7.py
#     A program to compute the total accummulation of the investment.

def main():
    print("This program calculates the accummulation of an investment")
    base = eval(input("Enter the fixed ammount every year: "))
    apr = eval(input("Enter the annual interest rate: "))
    years = eval(input("Enter the number of the years for investment"))
    principal = 0
    for i in range(years):
        principal = (base + principal)*(1+apr)
    print("The value in {} years is {}.".format(years,principal))

main()
