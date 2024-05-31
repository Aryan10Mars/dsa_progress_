# https://leetcode.com/problems/find-the-duplicate-number/

class Solution(object):
    def findDuplicate(self, nums):
        
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast :
                break
        
        slow = nums[0]

        while(slow != fast):
            slow = nums[slow]
            fast = nums[fast]
        
        return slow