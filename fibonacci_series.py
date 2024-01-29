# Fibonacci Series Code without recursion

def fibo(n):
    a=0
    b=1
    next=a+b
    while(n-1>0):
        a=b
        b=next
        next=a+b
        n-=1
    print(b)
n=int(input("Enter the number up to which you want to print the fibo series : "))
fibo(n)
        