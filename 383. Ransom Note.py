# 破题, 看了半天没明白意思, 明明很简单的东西说这么复杂
# 前一个字符串是后一个字符串的无顺序子串

from collections import Counter


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        dct = Counter(magazine)
        for c in ransomNote:
            if c not in dct or dct[c] == 0:
                return False
            dct[c] -= 1
        return True
