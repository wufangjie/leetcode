'''
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26

Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.
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
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        n = len(s)

        @memo
        def count_rec(i):
            if i >= n:
                return 1
            elif s[i] == '0':
                return 0
            elif s[i] not in {'1', '2'}:
                return count_rec(i + 1)
            else:
                if (i + 2 > n or (s[i] == '2' and s[i + 1] in {'7', '8', '9'})):
                    return count_rec(i + 2)
                else:
                    return count_rec(i + 1) + count_rec(i + 2)
        return count_rec(0)


if __name__ == '__main__':
    assert Solution().numDecodings('1111111') == 21
    assert Solution().numDecodings('10023') == 0
    assert Solution().numDecodings('1023') == 2
    assert Solution().numDecodings('') == 0
