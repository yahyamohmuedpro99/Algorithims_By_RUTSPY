l=[1,2,33]

def sum(arr):
    arr=arr.copy()
    if not arr:
        return 0
    else:
        return arr.pop() + sum(arr)
def sum2(arr):
    arr=arr.copy()
    if len(arr) == 0:
        return 0
    else:
        return arr[0] + sum(arr[1:])
    
def sum3(arr):
    if not arr:
        return 0
    else:
        return arr[-1]+sum(arr[:-1])

def max(arr):
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    else:
        sub_max = max(arr[1:])
        #we take the arr[0] bcz we slice from arr[1:] which mean we have to back to first element 
        return sub_max if sub_max > arr[0] else arr[0] 

arr=[10,20]
print(max(l))