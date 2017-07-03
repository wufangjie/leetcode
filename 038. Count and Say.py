'''
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.
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
def count_say_rec(n):
    if n < 2:
        return '1'
    else:
        temp = count_say_rec(n - 1)
        count = 1
        pre = temp[0]
        result = []
        for elem in temp[1:]:
            if pre == elem:
                count += 1
            else:
                result.append(str(count) + pre)
                count = 1
                pre = elem
        result.append(str(count) + pre)
        return ''.join(result)


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        return count_say_rec(n)


if __name__ == '__main__':
    assert Solution().countAndSay(0) == '1'
    assert Solution().countAndSay(1) == '1'
    assert Solution().countAndSay(6) == '312211'
