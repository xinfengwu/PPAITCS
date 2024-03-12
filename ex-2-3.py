# ex-2-3.py
#   A simple program to average three exam scores
#   Illustrates use of multiple input

def main():
    print("This program comptes the average of two exam scores.")
    score1,score2,score3 = eval(input("Enter two scores separated by comma: "))
    average = (score1+score2+score3)/3
    
    print("The average of the scores is:", average)

main()
