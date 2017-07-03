class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort(), s.sort()
        lg, ls = len(g), len(s)
        ret = i = j = 0
        while i < lg and j < ls:
            if g[i] <= s[j]:
                i += 1
                ret += 1
            j += 1
        return ret
