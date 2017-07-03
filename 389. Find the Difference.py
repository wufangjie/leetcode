from collections import Counter


class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        sc, tc = Counter(s), Counter(t)
        for k, v in tc.items():
            if k not in sc or sc[k] != v:
                return k
