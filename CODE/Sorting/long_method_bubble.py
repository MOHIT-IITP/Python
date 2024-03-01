# Sorting method 1
# Bubble sort



def sortting(lst):
    swapped=False
    for i in range(len(lst)-1):
        for j in range(len(lst)-1):
            if lst[j]>lst[j+1]:
                swapped=True
                lst[j],lst[j+1]=lst[j+1],lst[j]
        if not swapped:
            return 

list_input= input("Enter number with space : ")
lst=list_input.split(" ")
sortting(lst)
for elem in lst:
    print(elem)
    print('\n')
