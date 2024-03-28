# https://leetcode.com/problems/merge-k-sorted-lists/

class Solution(object):
    def mergeKLists(self, lists):
        op = []

        for i in lists:
            head = i
            while head is not None:
                op.append(head.val)
                head = head.next
        
        op.sort()

        p = ListNode(0)
        ptr = p

        for i in op:
            po = ListNode(i)
            ptr.next = po
            ptr = ptr.next
        
        return p.next