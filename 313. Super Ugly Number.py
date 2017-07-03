import heapq


class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        # to record last prime rather than calculate
        np = len(primes)
        H = [(1, 0)]
        while n:
            current, last = heapq.heapreplace(H, (H[0][0] * primes[np-1], np-1))
            # import pdb
            # pdb.set_trace()

            n -= 1
            if n == 0:
                return current

            for i in range(last, np - 1):
                heapq.heappush(H, (current * primes[i], i))




        # np = len(primes)
        # H = [1]
        # temp = list(range(np - 1, 0, -1))
        # while n:
        #     current = heapq.heapreplace(H, H[0] * primes[np - 1])
        #     n -= 1
        #     if n == 0:
        #         return current

        #     for i in temp:
        #         if current % primes[i]:
        #             heapq.heappush(H, current * primes[i - 1])
        #         else:
        #             break




import time
tic = time.time()
assert Solution().nthSuperUglyNumber(100000, [7,19,29,37,41,47,53,59,61,79,83,89,101,103,109,127,131,137,139,157,167,179,181,199,211,229,233,239,241,251]) == 1092889481
print(time.time() - tic)
