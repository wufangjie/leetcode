import heapq

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        H = [1]
        while H:
            current = heapq.heappop(H)
            n -= 1
            if n == 0:
                return current

            heapq.heappush(H, current * 5)
            if current % 5:
                heapq.heappush(H, current * 3)
                if current % 3:
                    heapq.heappush(H, current * 2)


print(Solution().nthUglyNumber(1690))
#Solution().nthUglyNumber(3)
