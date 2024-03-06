# this code is not working right  now but the process is kinda same 
def partition(a,start,end):
    pos=start
    for i  in range(start,end):
        if(a[i]<=a[end]):
            a[i],a[pos]=a[pos],a[i]
            pos+=1
    return pos-1

def quicksort(a,start,end):
    if(start>=end):
        return 
    pivot = partition(a,start,end)
    quicksort(a,start,pivot-1)
    quicksort(a,pivot,end)
    
    
a=[5,4,3,3,1,77]
quicksort(a,0,5)