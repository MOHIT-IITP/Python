def pattern(n): 
    for i in range(n, 0, -1):
        for j in range(0, n-i):
            print(end=" ")
        for j in range(0, i):
            print("*", end=" ")
        print()
    for row in range(n):
        for i in range(n-row-1):
            print(" ",end="")
        for i in range(0,row+1):
            print("*",end=" ")
        print()
n=int(input())
pattern(n)