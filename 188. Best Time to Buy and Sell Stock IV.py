import heapq


class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        if k == 0:
            return 0
        elif k == 1:
            return self.maxProfit_if_k_eq_1(prices)

        pairs = []
        sell = buy = prices[0]
        profit = 0
        for p in prices:
            if p >= sell:
                sell = p
            else:
                profit += sell - buy
                if sell != buy:
                    pairs.append((buy, sell))
                sell = buy = p
        if sell != buy:
            pairs.append((buy, sell))
            profit += sell - buy

        n = len(pairs)
        if k >= n:
            return profit

        def cal_del_pro(i, j):
            l = pairs[i][1] - pairs[i][0]
            r = pairs[j][1] - pairs[j][0]
            return l + r - max(pairs[j][1] - pairs[i][0], l, r)


        H = [(cal_del_pro(i, i+1), i, i+1) for i in range(n - 1)]
        heapq.heapify(H)
        near_dict = {i: [i-1, i+1] for i in range(n)}
        near_dict[0][0] = None
        near_dict[n-1][1] = None

        combined = 0
        while combined < n - k:
            v, i, j = heapq.heappop(H)
            if i in near_dict and j in near_dict:
                pairs.append(sorted(
                    ((pairs[i][0], pairs[j][1]), pairs[i], pairs[j]),
                    key=lambda x: x[0] - x[1])[0])
                end = n + combined
                l, r = near_dict[i][0], near_dict[j][1]
                near_dict[end] = [l, r]
                near_dict.pop(i)
                near_dict.pop(j)
                combined += 1
                profit -= v

                if l is not None:
                    near_dict[l][1] = end
                    heapq.heappush(H, (cal_del_pro(l, end), l, end))
                if r is not None:
                    near_dict[r][0] = end
                    heapq.heappush(H, (cal_del_pro(end, r), end, r))

        return profit

    def maxProfit_if_k_eq_1(self, prices):
        theMin = float('inf')
        max_profit = 0
        for p in prices:
            if p < theMin:
                theMin = p
            else:
                max_profit = max(max_profit, p - theMin)
        return max_profit


if __name__ == '__main__':
    prices = [1, 1, 8, 1, 4, 9, 8, 5, 9, 5, 5, 5, 7, 2, 6, 2, 2, 3, 5, 4, 3, 7]
    print(Solution().maxProfit(3, prices))
    # pairs = [(1, 8), (1, 9), (5, 9), (5, 7), (2, 6), (2, 5)]
    # profit = 28
    Solution().maxProfit(2, [4,2,1])
    Solution().maxProfit(0, [1,3])
