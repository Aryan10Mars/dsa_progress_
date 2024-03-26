# https://leetcode.com/problems/maximum-subarray/

class Solution(object):
    def maxSubArray(self, nums):
        maxi = float('-inf')
        sum = 0

        for i in range(len(nums)):
            sum += nums[i]

            if sum > maxi:
                maxi = sum
            
            if sum < 0:
                sum = 0

        return maxi