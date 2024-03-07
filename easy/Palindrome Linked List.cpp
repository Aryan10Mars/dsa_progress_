// https://leetcode.com/problems/palindrome-linked-list/description/

class Solution {
public:

    ListNode* reverseLinkedList(ListNode* head){
        ListNode* prev = NULL;
        ListNode* curr = head;
        ListNode* next = NULL;

        while(curr != NULL){
            next = curr->next;
            curr->next = prev;
            prev = curr;
            curr = next;
        }
        return prev;
    }

    bool isPalindrome(ListNode* head) {
        ListNode* slow = head;
        ListNode* fast = head;

        while(fast != NULL && fast->next != NULL){
            slow = slow->next;
            fast = fast->next->next;
 
        }

        ListNode* newHead = reverseLinkedList(slow);

        ListNode* first = head;
        ListNode* second = newHead;

        while(second != NULL){
            if (first->val != second->val){
                reverseLinkedList(newHead);

                return false;
            }

            first = first->next;
            second = second->next;

        }

        reverseLinkedList(newHead);

        return true;

    }
};