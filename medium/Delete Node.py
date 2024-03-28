# https://leetcode.com/problems/delete-node-in-a-linked-list/description/

class Solution(object):
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next