# https://leetcode.com/problems/maximum-depth-of-binary-tree/

class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        
        leftH = self.maxDepth(root.left)
        rightH = self.maxDepth(root.right)
        return max(leftH,rightH) + 1