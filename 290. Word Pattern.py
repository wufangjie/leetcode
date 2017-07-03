class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        split = str.split(' ')
        if len(pattern) != len(split):
            return False
        dict_p, dict_c = {}, {}
        for p, c in zip(pattern, split):
            if c != dict_p.setdefault(p, c):
                return False
            if p != dict_c.setdefault(c, p):
                return False
        return True


if __name__ == '__main__':
    assert Solution().wordPattern("abba", "dog cat cat dog") == True
    assert Solution().wordPattern("abba", "dog cat cat fish") == False
    assert Solution().wordPattern("aaaa", "dog cat cat dog") == False
    assert Solution().wordPattern("abba", "dog dog dog dog") == False
