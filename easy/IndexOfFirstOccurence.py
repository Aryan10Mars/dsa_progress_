# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

class Solution(object):
    def strStr(self, haystack, needle):
        
        if needle in haystack:
            return haystack.index(needle)
        return -1

        # for i in range(0, len(haystack) - len(needle) + 1):
        #     if haystack[i:i+len(needle)] == needle:
        #         return i
        
        # return -1