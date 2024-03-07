# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

class Solution(object):
    def removeNthFromEnd(self, head, N):
        
        fastp = head
        slowp = head

        for i in range(N):
            fastp = fastp.next

        if fastp is None:
            return head.next

        while fastp.next is not None:
            fastp = fastp.next
            slowp = slowp.next

        delNode = slowp.next
        slowp.next = slowp.next.next
        delNode = None
        return head