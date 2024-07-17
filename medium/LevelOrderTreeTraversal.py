# https://leetcode.com/problems/binary-tree-level-order-traversal/

class Solution(object):
    def levelOrder(self, root):
        if not root:
            return []

        output = []
        q = [root]

        while q:
            
            level = []

            for i in range(len(q)):
                
                node = q.pop(0)

                level.append(node.val)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            
            output.append(level)
            
        
        return output