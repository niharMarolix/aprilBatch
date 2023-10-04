# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.

def maxSubArray(nums):
    maxSum = -99999999999999999999999999999999999999999999999999
    start =0
    end = 0

    for i in range(len(nums)):
        currentSum = 0
        for j in range(i, len(nums)):
            currentSum = currentSum + nums[j]
            maxSum= max(maxSum, currentSum)
            if currentSum>maxSum:
                maxSum = currentSum
                start = i
                end  = j
    return(maxSum,nums[start:end+1])

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))



