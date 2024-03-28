# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/description/

arr = [int(i) for i in input().split(',')]
print(arr)


class Solution(object):
    def deleteMiddle(self, head):
        
        if head is None or head.next is None :
            return None

        slowp = head
        fastp = head.next.next if head.next else None

        while fastp and fastp.next :
            slowp = slowp.next
            fastp = fastp.next.next

        slowp.next = slowp.next.next
        return head