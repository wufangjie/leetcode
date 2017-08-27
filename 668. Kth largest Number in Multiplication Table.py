class Solution(object):
    def findKthNumber(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        def count_seperate(v):
            less = equal = 0
            i, j = 1, n
            while i <= m and j > 0:
                ixj = i * j
                if ixj > v:
                    j -= 1
                elif ixj < v:
                    i += 1
                    less += j
                else:
                    i += 1
                    j -= 1
                    equal += 1
                    less += j
            return less, less + equal

        lo, hi = 1, m * n
        while True:
            mid = (lo + hi) >> 1
            less, le = count_seperate(mid)
            if k <= less:
                hi = mid - 1
            elif le < k:
                lo = mid + 1
            else:
                return mid

        # # MLE
        # g = heapq.merge(*[[i * j for i in range(1, m + 1)]
        #                   for j in range(1, n + 1)])
        # while k > 1:
        #     next(g)
        #     k -= 1
        # return next(g)


        # # TLE
        # count = defaultdict(int)
        # for i in range(1, m + 1):
        #     for j in range(1, n + 1):
        #         count[i * j] += 1
        # for v, c in sorted(count.items()):
        #     k -= c
        #     if k <= 0:
        #         return v



# print(Solution().findKthNumber(3, 3, 5))
# print(Solution().findKthNumber(2, 3, 6))
# print(Solution().findKthNumber(2, 3, 1))

# print(Solution().findKthNumber(9895, 28405, 100787757))
print(Solution().findKthNumber(42, 34, 401), 126)
