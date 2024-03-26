# https://leetcode.com/problems/single-number/description/

class Solution(object):
    def singleNumber(self, nums):
        
        res = 0

        for num in nums:
            res ^= num

        return res