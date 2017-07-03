import re

reg = re.compile(r'([^ ]+)')


class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(reg.findall(s))

        # if not s:
        #     return 0
        # return sum((1 for i in range(len(s) - 1)
        #             if s[i] != ' ' and s[i + 1] == ' ')) + (s[-1] != ' ')



print(Solution().countSegments('   '))
print(Solution().countSegments(' 2  '))
print(Solution().countSegments(' 2  3'))
print(Solution().countSegments('1 2  3'))
print(Solution().countSegments('  2  '))
print(Solution().countSegments('  2  3'))
print(Solution().countSegments('1  2  3'))
print(Solution().countSegments('12  3'))
print(Solution().countSegments('12  3 '))
