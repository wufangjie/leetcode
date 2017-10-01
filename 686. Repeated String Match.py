import re


class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        if B in A:
            return 1
        elif B in A + A:
            return 2

        temp = re.search(r'(?:{})+'.format(A), B)
        if temp:
            a, b = temp.span()
            ret = (b - a) // len(A)
            if A.endswith(B[:a]) and A.startswith(B[b:]):
                if a != 0:
                    ret += 1
                if b != len(B):
                    ret += 1
                return ret
        return -1




print(Solution().repeatedStringMatch("abcd", "cdabcdab"))
print(Solution().repeatedStringMatch("abcd", "bcdabcd"))
