'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
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
def gen_rec(n):
    if n == 1:
        return {'()': True}
    result = {}
    for template in gen_rec(n - 1):
        for i in range(n + 1):
            result[template[:i] + '()' + template[i:]] = True
    return result


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return list(gen_rec(n))


if __name__ == '__main__':
    assert Solution().generateParenthesis(2)
