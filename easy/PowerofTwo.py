# https://leetcode.com/problems/power-of-two/

class Solution(object):
    def isPowerOfTwo(self, n): #boolean
        return n > 0 and n&(n-1) == 0