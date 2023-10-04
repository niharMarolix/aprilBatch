import math

def jumpSearch(arr,l,t):

    step = int(math.sqrt(l))
    prev = 0

    while arr[min(step,l)-1] < t:
        prev = step
        step = step +int(math.sqrt(l))
        if prev>=l:
            return("not found")
        
    for position in range(prev, min(step, l)):
        if arr[position] == t:
            return position
        
    return("not found")
        
arr = [1,3,2,4,7,6,5,9,8,20,10]
sortedArr = sorted(arr)
print(sortedArr)
l = len(arr)
t = 10
print(jumpSearch(sortedArr,l,t))