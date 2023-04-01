class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        l , r = 0, 1
        maxp = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                price = prices[r] - prices[l]
                maxp = max(maxp, price)
            else:
                r = l
            r+=1
        return maxp