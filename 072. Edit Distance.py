'''
Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

a) Insert a character
b) Delete a character
c) Replace a character
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
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n = len(word1) + len(word2)
        @memo
        def leven_rec(i1, i2):
            try:
                if word1[i1] == word2[i2]:
                    return leven_rec(i1 + 1, i2 + 1)
                else:
                    return min(leven_rec(i1 + 1, i2), leven_rec(i1, i2 + 1),
                               leven_rec(i1 + 1, i2 + 1)) + 1
            except IndexError:
                return n - i1 - i2
        return leven_rec(0, 0)


    def lcs_distance(self, word1, word2):
        '''
        insertion and deletion only
        '''
        @memo
        def lcs_rec(i1, i2):
            try:
                if word1[i1] == word2[i2]:
                    return lcs_rec(i1 + 1, i2 + 1) + 1
                else:
                    return max(lcs_rec(i1 + 1, i2), lcs_rec(i1, i2 + 1))
            except IndexError:
                return 0
        return len(word1) + len(word2) - lcs_rec(0, 0)


if __name__ == '__main__':
    assert Solution().minDistance('Starwalker', 'Starbuck') == 5
    assert Solution().minDistance('ab', 'bc') == 2
    assert Solution().minDistance('aeeeeb', 'dffffa') == 6
