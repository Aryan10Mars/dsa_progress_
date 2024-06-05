# https://leetcode.com/problems/longest-consecutive-sequence/

class Solution(object):
    def longestConsecutive(self, nums):

        n = len(nums)
        if n == 0:
            return 0

        nums.sort()
        lastSmaller = float('-inf')
        count = 0
        longest = 1

        for i in range(n):
            if nums[i] - 1 == lastSmaller:
                count += 1
                lastSmaller = nums[i]
            
            elif nums[i] != lastSmaller:
                count = 1
                lastSmaller = nums[i]
            
            longest = max(longest, count)

        return longest