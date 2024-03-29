# Reverse Singly Linked List

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    prev = None
    curr = head
    nextptr = None

    while curr is not None:
        nextptr = curr.next
        curr.next = prev
        prev = curr
        curr = nextptr

    head = prev
    return head
    
def StringToLinkedList(s):
    if not s:
        return


    dummy = ListNode()
    curr = dummy
    for val in s:
        print(val)
        curr.next = ListNode(val)
        curr = curr.next
    
    return dummy.next


inp = input("Enter the number: ")
inpList = inp.split()
print(inpList)
inpList = [int(i) for i in inpList]

print(inpList)

head = StringToLinkedList(inpList)
head = reverseList(head)

curr = head

while curr is not None:
    print(curr.val)
    curr = curr.next