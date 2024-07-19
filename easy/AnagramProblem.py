# https://leetcode.com/problems/valid-anagram/description/

class Solution(object):
    def isAnagram(self, s, t):
        return sorted(s) == sorted(t)