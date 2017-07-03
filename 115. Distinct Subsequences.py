'''
Given a string S and a string T, count the number of distinct subsequences of T in S.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Here is an example:
S = "rabbbit", T = "rabbit"

Return 3.
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
    def numDistinct_maximum_recursion_depth_exceeded(self, s, t):
        m, n = len(s), len(t)

        @memo
        def count_rec(i, j):
            if j == n:
                return 1
            elif i == m:
                return 0
            if s[i] == t[j]:
                return count_rec(i + 1, j + 1) + count_rec(i + 1, j)
            else:
                return count_rec(i + 1, j)

        return count_rec(0, 0) if n else 0


    def numDistinct_MLE(self, s, t):
        m, n = len(s), len(t)
        dd = {(i, n): 1 for i in range(m + 1)}
        dd.update({(m, j): 0 for j in range(n)})
        for j in range(n - 1, -1, -1):
            for i in range(m - 1, -1, -1):
                if s[i] == t[j]:
                    dd[i, j] = dd[i + 1, j + 1] + dd[i + 1, j]
                else:
                    dd[i, j] = dd[i + 1, j]
        return dd[0, 0]


    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        m, n = len(s), len(t)
        dp = [0] * n + [1]
        for i in range(m - 1, -1, -1):
            for j in range(n):
                if s[i] == t[j]:
                    dp[j] += dp[j + 1]
        return dp[0]


if __name__ == '__main__':
    assert Solution().numDistinct('rabbbit', 'rabbit') == 3
