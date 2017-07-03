'''
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
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
def climb_rec(n):
    if n < 2:
        return 1
    else:
        return climb_rec(n - 2) + climb_rec(n - 1)


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        return climb_rec(n)
