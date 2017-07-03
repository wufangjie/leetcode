'''
There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

    Each child must have at least one candy.
    Children with a higher rating get more candies than their neighbors.

What is the minimum candies you must give?
'''

class Solution(object):
    def candy_nlogn(self, ratings):
        """
        need sort
        use recursion will exceed maximum recursion depth
        """
        theSum, n = 0, len(ratings)
        seq = sorted(range(n), key=lambda x:ratings[x])
        ratings += [float('inf'), float('inf')]
        candy_dict = {}
        for i in seq:
            result = 1
            if ratings[i] > ratings[i + 1]:
                result = max(result, candy_dict[i + 1] + 1)
            if ratings[i] > ratings[i - 1]:
                result = max(result, candy_dict[i - 1] + 1)
            candy_dict[i] = result
            theSum += result

        return theSum


    # def candy(self, ratings):
    #     """
    #     :type ratings: List[int]
    #     :rtype: int
    #     """
    #     dir = 1
    #     n = len(ratings)
    #     theSum = 1
    #     idx_hi = 0
    #     lo = 1
    #     for i in range(1, n):
    #         if ratings[i] > ratings[i - 1]:
    #             if dir <= 0:
    #                 if lo < 1:
    #                     theSum += (1 - lo) * (i - idx_hi)
    #                 elif lo > 1:
    #                     theSum -= (lo - 1) * (i - idx_hi - 1)
    #                 lo = 2
    #                 dir = 1
    #             else:
    #                 lo += 1
    #         elif ratings[i] < ratings[i - 1]:
    #             if dir == 1:
    #                 idx_hi = i - 1
    #             dir = -1
    #             lo -= 1
    #         elif dir == 1:
    #             idx_hi = i - 1
    #             dir = 0
    #             lo -= 1
    #         theSum += lo
    #     if dir <= 0:
    #         if lo < 1:
    #             theSum += (1 - lo) * (n - idx_hi)
    #         elif lo > 1:
    #             theSum -= (lo - 1) * (n - idx_hi - 1)
    #     return theSum


if __name__ == '__main__':
    assert Solution().candy([9, 2, 4, 5, 1, 3, 6, 7]) == 18
    assert Solution().candy(range(12000, 0, -1)) == 72006000

    assert Solution().candy([1, 2, 2]) == 4
    assert Solution().candy([0, 1, 7, 7, 6, 6, 5, 4, 3, 2, 1]) == 30
