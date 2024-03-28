# https://leetcode.com/problems/rotate-list/description/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):
    def rotateRight(self, head, k):
        
        if head == None or head.next == None:
            return head

        temp = head
        length = 1
        
        while temp.next is not None:
            length += 1
            temp = temp.next
        
        # return length

        k = k % length

        for i in range(k):
            
            slow = head
            fast = head.next

            while fast.next:
                slow = slow.next
                fast = fast.next

            fast.next = head
            slow.next = None
            head=fast

        return head