class Solution(object):
    def maxProfit(self, prices):
        price = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                price += prices[i] - prices[i - 1]
        return price


prices = eval(input())

result = Solution().maxProfit(prices)

print(result)
