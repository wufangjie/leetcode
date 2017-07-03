'''
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

For example,
Given:
s1 = "aabcc",
s2 = "dbbca",

When s3 = "aadbbcbcac", return true.
When s3 = "aadbbbaccc", return false.
'''

from functools import wraps

def memo(func):
    cache = {}
    @wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    wrapper._cache = cache
    return wrapper


class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        l1, l2, l3 = map(lambda x: len(x), (s1, s2, s3))

        @memo
        def rec(i, j, k):
            if i == l1:
                return s2[j:] == s3[k:]
            elif j == l2:
                return s1[i:] == s3[k:]
            if s1[i] == s3[k] and rec(i + 1, j, k + 1):
                return True
            if s2[j] == s3[k] and rec(i, j + 1, k + 1):
                return True
            return False

        return rec(0, 0, 0)


if __name__ == '__main__':
    s1, s2, s3 = "abcd", "efg", "aefgbcd"
    Solution().isInterleave(s1, s2, s3)
