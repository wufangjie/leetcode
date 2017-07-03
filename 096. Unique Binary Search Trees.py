'''
Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

For example,
Given n = 3, there are a total of 5 unique BST's.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
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
def count_UBST(n):
    if n < 2:
        return 1
    count = 0
    for i in range(1, n + 1):
        count += count_UBST(i - 1) * count_UBST(n - i)
    return count


class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        return count_UBST(n)


if __name__ == '__main__':
    Solution().numTrees(3)
