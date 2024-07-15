# https://leetcode.com/problems/roman-to-integer/

class Solution(object):
    def romanToInt(self, s):
      dict = {
        'I' :1,
		'V' :5,
		'X' :10,
		'L' :50,
		'C' :100,
		'D' :500,
		'M' :1000
      }  

      s = s.replace("IV","IIII").replace("IX","VIIII")
      s = s.replace("XL","XXXX").replace("XC","XXXXXXXXX")
      s = s.replace("CD","CCCC").replace("CM","CCCCCCCCC")

      res = 0
      for char in s:
        res = res + dict[char]

      return res