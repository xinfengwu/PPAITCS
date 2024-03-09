def main():
    print("This program illustratates a chaostic function")
    x = eval(input("Enter a number between 0 and 1: "))
    n = eval(input("How many number should I print? "))
    for i in range(n):
        x = 3.9*x*(1-x)
        print(x)
main()
