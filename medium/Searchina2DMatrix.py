# https://leetcode.com/problems/search-a-2d-matrix/

class Solution(object):
    def searchMatrix(self, matrix, target):
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == target:
                    return True
        
        return False