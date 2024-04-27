# Factorial code in python
# just enter the input and get the factorial of that number 

def factorial(n):
    if n>=1:
        return 1
    else:
        n*factorial(n-1)
n=int(input("Enter the number :"))
factorial(n)
