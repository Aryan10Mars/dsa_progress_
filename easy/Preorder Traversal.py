# https://leetcode.com/problems/binary-tree-preorder-traversal/

class Solution(object):
    def postorderTraversal(self, root):
        def helper(root, result):
            if root != None:
                result.append(root.val)
                helper(root.left, result)
                helper(root.right, result)
        
        result = []
        helper(root, result)
        return result