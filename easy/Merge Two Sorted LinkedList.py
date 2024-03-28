# https://leetcode.com/problems/merge-two-sorted-lists/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        head  = ListNode(0)
        current = head

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            
            else:
                current.next = list2
                list2 = list2.next
            
            current = current.next
        
        current.next = list1 or list2

        return head.next