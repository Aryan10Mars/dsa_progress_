# https://leetcode.com/problems/minimum-path-sum/description/?orderBy=most_votes

class Solution(object):
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])
        self.memo = [[0] * n for _ in range(m)]
        return self.find(grid, m-1, n-1, self.memo)

    def find(self, grid, m, n, memo):
        if m == 0 and n == 0:
            return grid[0][0]
        elif m < 0 or n < 0:
            return float('inf')
        elif memo[m][n] != 0:
            return memo[m][n]

        memo[m][n] = grid[m][n] + min(self.find(grid, m-1, n, memo), self.find(grid, m , n-1, memo))

        return memo[m][n]