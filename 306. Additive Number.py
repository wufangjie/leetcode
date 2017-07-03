class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n = len(num)
        def rec(i, num1='', num2=''):
            if i == n:
                return False

            if num2 != '':
                if num2 != 0 and rec(i+1, num1, num2*10+int(num[i])):
                    return True
                while i < n:
                    num3 = str(num1 + num2)
                    if not num.startswith(num3, i):
                        break
                    num2, num1 = num1 + num2, num2
                    i += len(num3)
                else:
                    return True
            elif num1 != '':
                if num1 != 0 and rec(i+1, num1*10+int(num[i])):
                    return True
                return rec(i+1, num1, int(num[i]))
            else:
                return rec(i+1, int(num[i]))

        return rec(0)


assert Solution().isAdditiveNumber("112358")
assert Solution().isAdditiveNumber("199100199")
assert not Solution().isAdditiveNumber("1203")
assert not Solution().isAdditiveNumber("0235813")
assert not Solution().isAdditiveNumber("120122436")
