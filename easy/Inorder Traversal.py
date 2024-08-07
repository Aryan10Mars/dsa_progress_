# https://leetcode.com/problems/binary-tree-inorder-traversal/

class Solution(object):
    def postorderTraversal(self, root):
        def helper(root, result):
            if root != None:
                helper(root.left, result)
                result.append(root.val)
                helper(root.right, result)
        
        result = []
        helper(root, result)
        return result