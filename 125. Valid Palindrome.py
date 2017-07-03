import re
reg = re.compile(r'\W+')

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        clean_str = reg.sub('', s.lower())
        mid = len(clean_str) >> 1
        return clean_str[:mid] == clean_str[:-mid-1:-1]


if __name__ == '__main__':
    sol = Solution()
    assert sol.isPalindrome("")
    assert sol.isPalindrome("A man, a plan, a canal: Panama")
    assert not sol.isPalindrome("race a car")
