class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        if not prices:
            return 0

        profit = 0
        sell = buy = prices[0]
        for p in prices:
            if p >= sell:
                sell = p
            elif p < sell - fee:
                if sell - buy <= fee:
                    if p < buy:
                        sell = buy = p
                else:
                    profit += sell - buy - fee
                    sell = buy = p
            elif p < buy:
                buy = p
        return profit + max(0, sell - buy - fee)



print(Solution().maxProfit([1, 3, 2, 8, 4, 9], 2), 8)
print(Solution().maxProfit([9,8,7,1,2], 3), 0)
print(Solution().maxProfit([2,1,4,4,2,3,2,5,1,2], 1), 4)
