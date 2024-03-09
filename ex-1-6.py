
def main():
    print("This program illustratates a chaostic function")
    x = eval(input("Enter a number between 0 and 1: "))
    y=x
    z=x
    for i in range(10):
        x = 3.9*x*(1-x)
        print(x)
    print('-----------------------')
    for i in range(10):
        y = 3.9*(y-y*y)
        print(y)
    print('-----------------------')
    for i in range(10):
        z = 3.9*z-3.9*z*z
        print(z)
    print('-----------------------')
main()
