# https://leetcode.com/problems/odd-even-linked-list/description/

class Solution(object):
    def oddEvenList(self, head):
        if not head or not head.next:
            return head

        odd_head = head
        even_head = head.next
        odd_tail = head
        even_tail = head.next

        while even_tail and even_tail.next:
            odd_tail.next = even_tail.next
            odd_tail = odd_tail.next
            even_tail.next = odd_tail.next
            even_tail = even_tail.next

        odd_tail.next = even_head
        return odd_head