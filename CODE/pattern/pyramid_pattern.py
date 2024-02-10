# the output will be something like this    
#         *
#        ***
#       *****
#      *******
#     *********

def pattern(n):
    for row in range(n):
        for i in range(n-row-1):
            print(" ",end="")
        for i in range(row+1):
            print("*",end="")
        for i in range(row):
            print("*",end="")
        print("\n")
            
n=int(input())
pattern(n)