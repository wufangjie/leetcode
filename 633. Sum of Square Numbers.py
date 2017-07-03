class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        if c == 0:
            return True

        while c % 4 == 0:
            c //= 4

        hi = int(c ** 0.5) + 1
        lst1 = [i ** 2 for i in range(1, hi, 2)]
        lst2 = [i ** 2 for i in range(0, hi, 2)] if c & 1 else lst1
        l1, l2 = len(lst1), len(lst2)
        i1, i2 = 0, l2 - 1
        while i1 < l1 and i2 > -1:
            if lst1[i1] + lst2[i2] == c:
                return True
            elif lst1[i1] + lst2[i2] < c:
                i1 += 1
            else:
                i2 -= 1
        return False



# print(Solution().judgeSquareSum(37))
# print(Solution().judgeSquareSum(3))
# print(Solution().judgeSquareSum(2))
# print(Solution().judgeSquareSum(58))
# print(Solution().judgeSquareSum(57))
print(Solution().judgeSquareSum(0)) # NOTE: infinite loop % 4
