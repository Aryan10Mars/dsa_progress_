# https://leetcode.com/problems/set-matrix-zeroes/

class Solution(object):
    def setZeroes(self, matrix):
        row = set()
        column = set()

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row.add(i)
                    column.add(j)


        for i in row:
            for j in range(len(matrix[0])):
                matrix[i][j] = 0

        for i in column:
            for j in range(len(matrix)):
                matrix[j][i] = 0