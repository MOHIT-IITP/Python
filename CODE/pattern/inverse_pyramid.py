# the output will be something like this    
#     *********
#      *******
#       *****
#        ***
#         *

def pattern(rows):
    for i in range(rows, 0, -1):
        for j in range(0, rows - i):
            print(end=" ")
        for j in range(0, i):
            print("*", end=" ")
        print()

n=int(input())
pattern(n)
