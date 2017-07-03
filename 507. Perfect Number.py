class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 2:
            return False
        num2 = num
        theSum = 2 * num
        i = 2
        while True:
            count = 0
            while num2 != 1:
                if num2 % i == 0:
                    num2 //= i
                    count += 1
                else:
                    break

            if count:
                j = (i ** (count + 1) - 1) // (i - 1)
                if theSum % j != 0:
                    return False
                theSum //= j
                if theSum < 1 + num2:
                    return False
            i += (1 if i == 2 else 2)

            if i ** 2 > num2:
                return theSum == 1 + num2


print(Solution().checkPerfectNumber(28))
assert not Solution().checkPerfectNumber(1)
assert not Solution().checkPerfectNumber(0)


# <==> num's all factor include self equals to 2 * num
# if a ** b | num, then (a ** (b + 1) - 1) // (a - 1) | theSum, then recursive the left
