def bubblesort(lst):
    n=len(lst)
    for i in range(n-1,0,-1):
        for j in range(i):
            if lst[j]>lst[j+1]:
                lst[j],lst[j+1]=lst[j+1],lst[j]
    return lst
lst=[43,12,45,6234,76,34,76,23,87,23,99]


# i call the function with print because in neovim(macos) it works like this 
print(bubblesort(lst))
