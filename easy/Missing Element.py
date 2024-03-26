# https://leetcode.com/problems/missing-number/

class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        summation = (n*(n+1)) // 2
        a = sum(nums)

        missing = summation - a
        return missing