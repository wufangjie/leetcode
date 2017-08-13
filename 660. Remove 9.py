count = [9 ** i for i in range(10)]


class Solution(object):
    def newInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        ret, i = 0, 9
        while n:
            if n >= count[i]:
                ret += (n // count[i]) * 10 ** i
                n %= count[i]
            i -= 1
        return ret

print(Solution().newInteger(10))
