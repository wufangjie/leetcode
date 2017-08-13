class Solution(object):
    def newInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = [9 ** i for i in range(10)]

        ret = 0
        i = 9
        while n:
            if n >= count[i]:
                ret += (n // count[i]) * 10 ** i
                n %= count[i]
                # if n == 0:
                #     break
            i -= 1

        return ret

print(Solution().newInteger(10))
