# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):

        while True:
            if root.val > p.val and root.val > q.val:
                root = root.left
            
            elif root.val < p.val and root.val < q.val:
                root = root.right
            
            else:
                return root