# https://leetcode.com/problems/string-to-integer-atoi/

class Solution(object):
    def myAtoi(self, s):
        MIN, MAX = -2 ** 31, 2 ** 31 - 1
        n, empty, sign = 0, True, 1  
        for c in s:
            if empty:
                if c == ' ': continue  
                elif c == '-': sign = -1  
                elif c.isdigit(): n = int(c)
                elif c != '+': return 0
                empty = False
            else:
                if c.isdigit():
                    n = n * 10 + int(c)
                    if sign * n > MAX: return MAX
                    elif sign * n < MIN: return MIN
                else: break   
        return sign * n











        # res = 0
        # i = 0
        # sign = 1

        # while i < len(s) and s[i] == ' ':
        #     i += 1

        # if i < len(s) and (s[i] == '-' or s[i] == '+'):
        #     sign = -1 if s[i] == '-' else 1
        #     i += 1
        
        # while i<len(s) and '0' <= s[i] <= '9':
        #     res = res * 10 + (ord(s[i]) - ord('0'))
        #     i += 1
        
        # return res*sign