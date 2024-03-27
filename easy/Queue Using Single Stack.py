# https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue(object):

    def __init__(self):
        # Initialize an empty list to represent the queue using a stack
        self.stack = []

    def push(self, x):
        # Push (enqueue) the element to the end of the list (top of the stack)
        self.stack.append(x)
        

    def pop(self):
       # Pop (dequeue) the element from the front of the list (bottom of the stack) 
       return self.stack.pop(0)
        

    def peek(self):
        # Return the element at the front of the list without removing it
        return self.stack[0]
        

    def empty(self):
        # Check if the list (stack) is empty
        return len(self.stack) == 0