# https://leetcode.com/problems/diameter-of-binary-tree/

class Solution(object):
    def diameterOfBinaryTree(self, root):
        def depth(node):
            if not node:
                return 0
            
            left = depth(node.left)
            right = depth(node.right)
            return 1 + max(left, right)
        
        return depth(root.left) + depth(root.right)