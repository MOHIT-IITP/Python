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
        for i in range(0,row+1):
            print("*",end=" ")
        print()
            
n=int(input())
pattern(n)