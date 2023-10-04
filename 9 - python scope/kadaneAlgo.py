def maxSubArray(nums):
    maxEnd = nums[0]
    maxSumTillNow = nums[0]
    start = 0
    end = 0
    tempStart = 0

    for i in range(1,len(nums)):
        if nums[i]>maxEnd+nums[i]:
            maxEnd = nums[i]
            tempStart = i
        else:
            maxEnd = maxEnd+nums[i]
        if maxEnd>maxSumTillNow:
            maxSumTillNow= maxEnd
            start = tempStart
            end = i

    return(maxSumTillNow, nums[start:end+1])
        
nums = [-2,1,-3,4,-1,2,1,-5,4]
# print(sum(nums))
print(maxSubArray(nums))



