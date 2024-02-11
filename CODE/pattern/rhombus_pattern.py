# The output of the code will be something like this 
# *****
#  *****
#   *****
#    *****
#     *****

def pattern(n):
    for i in range(n):
        for j in range(0,i):
            print(" ",end="")
        for k in range(n):
            print("*",end="")
        print()
n=int(input())
pattern(n)