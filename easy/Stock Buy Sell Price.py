# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution(object):
    def maxProfit(self, prices):
        maxP = 0
        minP = float("inf")

        for i in range(len(prices)):
            minP = min(minP, prices[i])
            maxP = max(maxP, prices[i] - minP)

        return maxP