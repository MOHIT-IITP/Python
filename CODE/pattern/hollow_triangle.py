# The output of this code is  something like this 
#    *
#   * *
#  *   *  
# *     *
#* * * * *

def print_hollow_triangle(n):
    for i in range(n): 
        for j in range((2 * n) - 1):  
            if i == n - 1 or i + j == n - 1 or j - i == n - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()

rows = int(input("Enter the number of rows for the triangle: "))
print_hollow_triangle(rows)



