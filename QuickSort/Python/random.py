l=[1,2,3,4,6]

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

print(sum3(l))