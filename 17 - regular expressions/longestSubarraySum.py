'''
Given an integer array nums, find the 
subarray
 with the largest sum, and return its sum.

 Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
'''
def maxSubArraySumAndTheArray(nums):
    maxSum = -999999999999999999999999999999999
    maxSubaraay = []
    l = len(nums)
    for i in range(l):
        currentSum = 0
        currentSubArrau = []

        for j in range(i,l):

            currentSum = currentSum + nums[j]
            currentSubArrau.append(nums[j])

            if currentSum>maxSum:
                maxSum = currentSum
                maxSubaraay = currentSubArrau.copy()

    print(maxSum)
    print(maxSubaraay)

nums = [-2,1,-3,4,-1,2,1,-5,4]
maxSubArraySumAndTheArray(nums)
