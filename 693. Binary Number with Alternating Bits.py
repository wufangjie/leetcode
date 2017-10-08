class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        strn = bin(n)
        for c in strn[2::2]:
            if c != '1':
                return False
        for c in strn[3::2]:
            if c != '0':
                return False
        return True


print(Solution().hasAlternatingBits(5))
print(Solution().hasAlternatingBits(7))
