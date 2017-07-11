from utils import memo


class Solution(object):
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        n = len(special)

        @memo
        def dfs(i, *left):
            if i == n:
                return sum(p * l for p, l in zip(price, left))

            ret = dfs(i + 1, *left)
            sp = special[i][:-1]
            can_buy = [left[j] // v for j, v in enumerate(sp) if v > 0]
            if can_buy:
                buy = min(can_buy)
                if buy:
                    left = list(left)
                    paid = 0
                    for _ in range(buy):
                        paid += special[i][-1]
                        for j, v in enumerate(sp):
                            left[j] -= v
                        ret = min(ret, paid + dfs(i + 1, *left))
            return ret

        return dfs(0, *needs)


        # m, n = len(price), len(special)
        # inf = float('inf')

        # @memo
        # def dfs(i, *left):
        #     if i == n:
        #         return sum(p * l for p, l in zip(price, left))

        #     ret = dfs(i + 1, *left)
        #     can_remove = inf
        #     rms = []
        #     for j in range(m):
        #         if special[i][j] > 0:
        #             temp = left[j] // special[i][j]
        #             if temp == 0:
        #                 return ret
        #             elif temp < can_remove:
        #                 can_remove = temp
        #             rms.append(j)

        #     if can_remove != inf:
        #         left = list(left)
        #         bought = 0
        #         for k in range(can_remove):
        #             bought += special[i][-1]
        #             for j in rms:
        #                 left[j] -= special[i][j]
        #             ret = min(ret, bought + dfs(i + 1, *left))
        #     return ret

        # return dfs(0, *needs)



assert Solution().shoppingOffers([2,5], [[3,0,5],[1,2,10]], [3,2]) == 14
assert Solution().shoppingOffers([2,3,4], [[1,1,0,4],[2,2,1,9]], [1,2,1]) == 11
