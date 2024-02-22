# Sorting method
# Selection sort
import datetime

x1= (datetime.datetime.now())

def sorting(lst, size):
    for i in range(size):
        min_index = i
        for j in range(i + 1, size):
            if lst[j] < lst[min_index]:
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]

list_input=input("Enter the number with space  ")
lst=list_input.split(" ")
size = len(lst)
sorting(lst, size)
print(lst)

x2 = (datetime.datetime.now())
print("Time take by code is " , x2-x1)