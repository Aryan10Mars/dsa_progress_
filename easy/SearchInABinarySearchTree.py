# https://leetcode.com/problems/search-in-a-binary-search-tree/

class Solution(object):
    def searchBST(self, root, val):
        temp = root
        while temp:
            if temp.val == val:
                return temp

            elif temp.val < val:
                temp = temp.right

            else:
                temp = temp.left
        
        return None