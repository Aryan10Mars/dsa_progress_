# https://leetcode.com/problems/max-consecutive-ones/

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        count = 0
        max_count = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            elif nums[i] == 0:
                count = 0
            
            max_count = max(max_count, count)
        return max_count