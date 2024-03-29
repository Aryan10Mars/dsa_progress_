class ListNode(object):
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def reverseList(head):
    temp = head
    prev = None
    
    while temp:
        front = temp.next
        temp.next = prev
        prev = temp
        temp = front

    head = prev
    return head

def StringtoLinkedList(s):

    if not s:
        return

    dummy = ListNode()
    curr = dummy
    
    for val in s:
        print(val)
        curr.next = ListNode(val)
        curr = curr.next
    
    return dummy.next

inp = input("Enter a string : ")
inpList = inp.split()
print(inpList)
inpList = [int(i) for i in inpList]

print(inpList)
print()

head =  StringtoLinkedList(inpList)
print()
head = reverseList(head)

curr = head

while curr is not None:
    print(curr.val)
    curr = curr.next










