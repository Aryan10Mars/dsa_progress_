# https://leetcode.com/problems/binary-tree-right-side-view/

class Solution(object):
    def rightSideView(self, root):
        if not root:
            return []

        output = []
        q = [root]

        while q:
            p = len(q)
            for i in range(p):
                node = q.pop(0)

                if i == p - 1:
                    output.append(node.val)
                
                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
        
        return output