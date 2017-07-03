'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
'''

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        sell = buy = prices[0]
        profit = 0
        for p in prices:
            if p >= sell:
                sell = p
            else:
                profit += sell - buy
                sell = buy = p
        return profit + sell - buy

if __name__ == '__main__':
    Solution().maxProfit([7, 1, 5, 3, 6, 4])
