# ex-2-5.py
#    A program to convert Celsius temps to Fahrenheit
# by: Susan Computewell

def main():
    for i in range(0,101,10):
	    celsius = i
	    fahrenheit = 9/5 * celsius +32
	    print("The temperature is", fahrenheit, "degree Fahrenheit.")

main()

