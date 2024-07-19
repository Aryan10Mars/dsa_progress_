# https://leetcode.com/problems/permutations/

class Solution(object):
    def permute(self, nums):
        return list(itertools.permutations(nums))