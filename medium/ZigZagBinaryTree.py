# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

class Solution(object):
    def zigzagLevelOrder(self, root):
        if not root:
            return []

        output = []
        q = [root]
        i = 0

        while q:
            level_size = len(q)
            level = []
            for j in range(level_size):
                node = q.pop(0)

                level.append(node.val)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            if i % 2 != 0:
                output.append(level[::-1])
            else:
                output.append(level)
            
            i += 1

        return output