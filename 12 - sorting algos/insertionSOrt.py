def insertionSort(arr,l):
    for i in range(1,l):
        currentElement  = arr[i]
        j = i-1

        while j>=0 and arr[j]>currentElement:
            arr[j+1] = arr[j]
            j = j-1

        arr[j+1] = currentElement

    return arr


arr = [5,1,9,4,2]
l = len(arr)
print(insertionSort(arr,l))