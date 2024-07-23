# https://leetcode.com/problems/maximum-product-subarray/

class Solution(object):

    def maxProduct(self, nums):

        maxn = nums[0]
        minn = nums[0]
        result = nums[0]

        for num in nums[1:]:
            maxn *= num
            minn *= num
            maxn, minn = max(maxn, minn, num), min(maxn, minn, num)
            result = max(maxn, result)
        
        return result