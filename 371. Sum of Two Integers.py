class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        if a == -b:
            return 0

        if (a < 0 and abs(a) < b) or (b < 0 and (abs(b) < a)): # 3, -1 example
            sign = 1
            a, b = -a, -b
        else:
            sign = 0

        while b != 0:
            a, b = a ^ b, (a & b) << 1
        return -a if sign else a


print(Solution().getSum(1, -1))
print(Solution().getSum(43, 890))
print(Solution().getSum(43, -890))
print(Solution().getSum(3, -1))
print(Solution().getSum(-3, -3))

# I dont know if -b means use '-'
