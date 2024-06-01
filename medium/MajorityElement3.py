# https://leetcode.com/problems/majority-element-ii/

class Solution(object):
    def majorityElement(self, nums):
        element_count = Counter(nums)

        majority_elements = []
        threshold = len(nums)//3

        for element, count in element_count.items():
            if count > threshold:
                majority_elements.append(element)
        
        return majority_elements