def binarySearch(arr,l,t):
    startIndex = 0
    endIndex = l-1

    while endIndex >= startIndex:
        mid = (startIndex+endIndex)//2

        if arr[mid] == t:
            return mid
        
        elif arr[mid] >  t:
            endIndex = mid-1

        elif arr[mid] < t:
            startIndex = mid+1

    else:
        return("not found")



arr = [1,3,2,4,7,6,5,9,8,20,10]
sortedArr = sorted(arr)
print(sortedArr)
l = len(arr)
t = 10
print(binarySearch(sortedArr,l,t))