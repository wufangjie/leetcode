from functools import reduce
import bisect


class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        seen = []
        while n:
            current = n % 10
            n //= 10
            if seen and seen[-1] > current:
                i = bisect.bisect_right(seen, current)
                l = len(seen)
                ret = n * 10 ** (l + 1) + seen[i] * 10 ** l
                seen[i] = current
                ret += reduce(lambda x, y: 10 * x + y, seen)
                return -1 if ret > 2147483647 else ret
            else:
                bisect.insort(seen, current)
        return -1

# return number must a positive 32-bit integer
assert Solution().nextGreaterElement(12) == 21
assert Solution().nextGreaterElement(21) == -1
