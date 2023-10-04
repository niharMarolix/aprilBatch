def twoSum(a,t):
    start = 0
    end = len(a)-1

    while start < end:
        currentSum = a[start] + a[end]
        if currentSum ==t:
            return([start,end])
        elif currentSum<target:
            start = start+1
        elif currentSum>target:
            end = end-1

    return None
    # for i in range(len(a)):
    #     for j in range(i+1,len(a)):
    #         if a[i]+a[j]==target:
    #             return ([i,j])


nums = [5,6,7,1,9,2]
target = 9
print(twoSum(nums, target))


# O(1)
# O(logN)
# O(NlogN)