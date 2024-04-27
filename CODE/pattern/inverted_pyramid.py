# the output will be something like this 
# **********
# *********
# ********
# *******
# ******
# *****
# ****
# ***
# **
# *

def pattern(row):
    for i in range(row,0,-1):
        for j in range(i,0,-1):
            print("*",end="")
        print()
row=int(input("Enter the number of row: "))
pattern(row)