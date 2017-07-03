class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n != 1:
            if n == 3:
                return count + 2
            elif n & 0b1 == 0b0:
                count += 1
                n >>= 1
            elif n & 0b10 == 0b0:
                count += 2
                n >>= 1
            else:
                count += 2
                n = (n + 1) >> 1
        return count


print(Solution().integerReplacement(8))
print(Solution().integerReplacement(7))
print(Solution().integerReplacement(3))
