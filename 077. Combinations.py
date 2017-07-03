'''
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
'''

from itertools import combinations


from functools import wraps
from copy import deepcopy

def memo(func):
    cache = {}
    @wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    wrapper._cache = cache
    return wrapper


@memo
def comb_rec(n, k):
    if k == 0 or n < k:
        return []
    elif k == 1:
        return [[i] for i in range(1, n + 1)]
    result = deepcopy(comb_rec(n - 1, k - 1))
    for comb in result:
        comb.append(n)
    return comb_rec(n - 1, k) + result


class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        return [list(elem) for elem in combinations(range(1, n + 1), k)]


    def my_combine(self, n, k):
        return comb_rec(n, k)


if __name__ == '__main__':
    print(Solution().combine(5, 2))
