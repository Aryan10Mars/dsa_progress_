# https://leetcode.com/problems/move-zeroes/

class Solution(object):
    def moveZeroes(self, nums):
        snowballSize = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                snowballSize += 1
            
            elif snowballSize > 0:
                t = nums[i]
                nums[i] = 0
                nums[i-snowballSize] = t