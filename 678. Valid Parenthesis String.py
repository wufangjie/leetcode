from utils import memo


class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)

        # @memo # add memo is useless
        def dfs(count_left, i):
            if count_left < 0:
                return False
            while i < n:
                c = s[i]
                i += 1
                if c == ')':
                    if count_left == 0:
                        return False
                    count_left -= 1
                elif c == '(':
                    count_left += 1
                else:
                    nLeft, nRight = s.count('(', i), s.count(')', i)
                    nStar = n - i - nLeft - nRight + 1
                    if abs(nLeft + count_left - nRight) > nStar:
                        return False
                    return (dfs(count_left + 1, i)
                            or dfs(count_left, i)
                            or dfs(count_left - 1, i))
            return count_left == 0
        return dfs(0, 0)


# print(Solution().checkValidString('**))((**'))
# print(Solution().checkValidString('**))((*'))
print(Solution().checkValidString("(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())"))

print(Solution().checkValidString("(*)"), True)
