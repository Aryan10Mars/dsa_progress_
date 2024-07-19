# https://leetcode.com/problems/balanced-binary-tree/

class Solution(object):

    def height(self, root):
        if not root:
            return 0

        return max(self.height(root.left), self.height(root.right))+1

    def isBalanced(self, root):
        if not root:
            return True

        heightL = self.height(root.left)
        heightR = self.height(root.right)

        if(self.isBalanced(root.left) and self.isBalanced(root.right) and abs(heightL - heightR) <= 1):

            return True
    
        return False