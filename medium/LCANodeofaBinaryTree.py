# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if not root or root == p or root == q:
            return root
        
        l = self.lowestCommonAncestor(root.left, p , q)
        r = self.lowestCommonAncestor(root.right, p ,q)

        if l and r:
            return root
        
        return l or r