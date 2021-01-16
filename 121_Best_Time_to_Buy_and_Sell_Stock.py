#time - O(N)
#space - O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        minBuy = prices[0]
        ans = 0
        for i in range(1, len(prices)):
            ans = max(prices[i] - minBuy, ans)
            minBuy = min(minBuy, prices[i])
        return ans
