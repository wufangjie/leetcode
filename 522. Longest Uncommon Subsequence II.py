from collections import Counter


class Solution(object):
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        dct = Counter(strs)
        longer = set()
        for s in sorted(dct.keys(), key=lambda x: (-len(x), dct[x])):
            if dct[s] == 1:
                for s0 in longer:
                    if self.is_in(s, s0):
                        break
                else:
                    return len(s)
            longer.add(s)
        return -1

    @staticmethod
    def is_in(s, s0):
        n, n0 = len(s), len(s0)
        if n == n0:
            return False
        i = j = 0
        while n - i <= n0 - j:
            if s[i] == s0[j]:
                i += 1
                if i == n:
                    return True
            j += 1
        return False

assert Solution().findLUSlength(["aba","cdc","eae"]) == 3
