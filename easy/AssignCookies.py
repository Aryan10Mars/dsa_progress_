# https://leetcode.com/problems/assign-cookies/

class Solution(object):
    def findContentChildren(self, g, s):

        count = 0

        g.sort()
        s.sort()

        m, n = len(g), len(s)

        i = 0
        j = 0

        while i < m and j < n:

            if g[i] <= s[j]:
                i += 1
                j += 1
                count += 1

            elif g[i] > s[j]:
                j += 1
        
        return count