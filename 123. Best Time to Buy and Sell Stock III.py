'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
'''

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        def get_left():
            theMin = float('inf')
            max_profit = 0
            result = []
            for i, p in enumerate(prices):
                if p < theMin:
                    theMin = p
                elif p - theMin > max_profit:
                    result.append((i, p - theMin))
                    max_profit = p - theMin
            return result

        def get_right():
            theMin = float('inf')
            max_profit = 0
            result = []
            for i in range(len(prices) - 1, -1, -1):
                p = -prices[i]
                if p < theMin:
                    theMin = p
                elif p - theMin > max_profit:
                    result.append((i, p - theMin))
                    max_profit = p - theMin
            return result

        left, right = get_left(), get_right()
        i2 = len(right) - 1
        theBest = 0
        for i1, v1 in left:
            while i2 > -1:
                if right[i2][0] > i1:
                    break
                i2 -= 1
            else:
                break
            theBest = max(theBest, v1 + right[i2][1])
        return max(theBest, left[-1][1] if left else 0)


if __name__ == '__main__':
    Solution().maxProfit([1, 1, 8, 1, 4, 9, 8, 5, 9, 5, 5, 5, 7, 2, 6, 2, 2, 3, 5, 4])
