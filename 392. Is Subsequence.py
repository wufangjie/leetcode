class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s:
            return True

        ls, lt = len(s), len(t)
        i = j = 0
        while j < lt:
            if s[i] == t[j]:
                i += 1
                if i == ls:
                    return True
            j += 1
        return False


# Trie for follow up
