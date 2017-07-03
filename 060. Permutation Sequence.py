'''
The set [1,2,3,…,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):

    "123"
    "132"
    "213"
    "231"
    "312"
    "321"

Given n and k, return the kth permutation sequence.

Note: Given n will be between 1 and 9 inclusive.
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


@memo
def count_perm(n):
    if n < 2:
        return 1
    else:
        return n * count_perm(n - 1)


class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        count = {i: count_perm(i) for i in range(n + 1)}
        choices = [str(i) for i in range(1, n + 1)]
        result = []
        k -= 1
        while k != 0:
            idx, k = k // count[n - 1], k % count[n - 1]
            result.append(choices[idx])
            del choices[idx]
            n -= 1
        result.extend(choices)
        return ''.join(result)


if __name__ == '__main__':
    assert Solution().getPermutation(9, 3)
