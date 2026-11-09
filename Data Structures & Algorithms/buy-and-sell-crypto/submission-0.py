class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        result = 0
        right = 1
        while right < len(prices):
            if prices[left] < prices[right]:
                dif = prices[right] - prices[left]
                result = max(dif, result)
            else: left = right
            right += 1

        return result