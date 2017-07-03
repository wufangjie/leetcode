'''
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?
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
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        @memo
        def n_choose_k(n, k):
            if k == n or k == 0:
                return 1
            return n_choose_k(n - 1, k - 1) + n_choose_k(n - 1, k)
        return [n_choose_k(rowIndex, i) for i in range(rowIndex + 1)]


if __name__ == '__main__':
    Solution().getRow(10)
