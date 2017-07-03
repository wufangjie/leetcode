# num is positive

class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        full, num2 = 0, num
        while num2:
            num2 >>= 1
            full = (full << 1) + 1
        return full ^ num


print(Solution().findComplement(5))
print(Solution().findComplement(0))
