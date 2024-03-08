# https://leetcode.com/problems/intersection-of-two-linked-lists/

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        
        if headA is None or headB is None:
            return None

        pa = headA
        pb = headB
        countera = 0
        counterb = 0

        while pa is not None or pb is not None:
            if pa is not None:
                pa = pa.next
                countera += 1 
            
            if pb is not None:
                pb = pb.next
                counterb += 1
        
        pa = headA
        pb = headB
        
        while countera < counterb:
            pb = pb.next
            counterb -= 1
        
        while countera > counterb:
            pa = pa.next
            countera -= 1
        
        while pa is not None and pb is not None and pa != pb:
            pa = pa.next
            pb = pb.next

        return pa