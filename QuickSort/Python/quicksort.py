"""
quicksort is divided the arr into two greater than and lesser than [pivot]
and then quicksort those 2 arrays again 

"""

def quicksort(arr):
   
    #base case
    if len(arr) < 2:
        return arr
    pivot =arr[0]
    less=[i for i in arr[1:] if i < pivot]
    greater=[i for i in arr[1:] if i > pivot]

    return quicksort(less)+ [pivot] + quicksort(greater)
l=[1,5,6,9,8,4]
print(quicksort(l))