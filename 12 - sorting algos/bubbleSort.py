def bubbleSort(arr,l):
    for i in range(l):
        for j in range(0,l-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]= arr[j+1],arr[j]
               
    return arr

arr = [5,1,9,4,2]
l = len(arr)
print(bubbleSort(arr,l))