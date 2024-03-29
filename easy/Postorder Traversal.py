# https://leetcode.com/problems/binary-tree-postorder-traversal/

class Solution(object):
    def postorderTraversal(self, root):
        def helper(root, result):
            if root != None:
                helper(root.left, result)
                helper(root.right, result)
                result.append(root.val)
        
        result = []
        helper(root, result)
        return result