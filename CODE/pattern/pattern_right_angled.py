# pattern using python 

def pattern(n):
    for i in range(n):
        for j in range(i):
            print("*",end = "")
        print("\n")

n=int(input("Enter the number : "))
pattern(n)