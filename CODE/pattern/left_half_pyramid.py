# the output will be something like this 

#         *
#        **
#       ***
#      ****
#     *****
#    ******
#   *******
#  ********
# *********
def pattern(row):
    for i in range(row):
        for j in range(row-i-1):
            print(" ",end="")
        for k in range(i):
            print("*",end="")
        print()

row = int(input("Enter the Number : "))
pattern(row)
