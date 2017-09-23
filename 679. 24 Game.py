from itertools import combinations
import bisect


_cache = {}

def _judgePoint24(*nums):
    n = len(nums)
    if n == 1:
        return abs(nums[0] - 24) < 1e-7
        # return nums[0] == 24

    if nums in _cache:
        return _cache[nums]

    for pair in set(combinations(nums, 2)): # use set or not
        left = []
        i = j = 0
        while i < 2:
            if pair[i] == nums[j]:
                i += 1
            else:
                left.append(nums[j])
            j += 1
        left.extend(nums[j:])

        a, b = pair
        news = [a + b, a * b, a - b, b - a]
        a += 0.0 # NOTE
        if b != 0:
            news.append(a / b)
        if a != 0:
            news.append(b / a)
        for new in news:
            i = bisect.bisect(left, new)
            if i > 0:
                temp = left[:i] + [new]
            else:
                temp = [new]
            if i < n:
                temp += left[i:]
            if _judgePoint24(*temp):
                _cache[nums] = True
                return True
    _cache[nums] = False
    return False


# from utils import memo
# add = lambda x, y: x + y
# sub = lambda x, y: x - y
# mul = lambda x, y: x * y
# div = lambda x, y: x / y

# @memo
# def _judgePoint24(*nums):
#     if len(nums) == 1:
#         return True if nums[0] == 24 else False
#     for seq in set(permutations(nums)):
#         for op in [add, sub, mul, div]:
#             try:
#                 new = op(*seq[:2])
#             except ZeroDivisionError:
#                 continue
#             if _judgePoint24(new, *seq[2:]):
#                 return True
#     return False


class Solution(object):
    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return _judgePoint24(*sorted(nums))
        # return _judgePoint24(*sorted(Fraction(i) for i in nums))
        # return _judgePoint24(*[Fraction(i) for i in nums])


import time
tic = time.time()
print(Solution().judgePoint24([4, 1, 8, 7]))

print(Solution().judgePoint24([3, 3, 7, 7]))
print(Solution().judgePoint24([1, 3, 4, 6]))

print(Solution().judgePoint24([-3, 10, 1, 1]))

print(Solution().judgePoint24([8, 1, 6, 6]))
print(time.time() - tic)





########################################################################
# return the process
########################################################################
from itertools import permutations
from fractions import Fraction


_cache_process = {}


def _judgePoint24_process(*nums):
    n = len(nums)
    if n == 1:
        return '\n' if nums[0] == 24 else ''
    if nums in _cache_process:
        return _cache_process[nums]

    for pair in set(combinations(nums, 2)):
        left = []
        i = j = 0
        while i < 2:
            if pair[i] == nums[j]:
                i += 1
            else:
                left.append(nums[j])
            j += 1
        left.extend(nums[j:])

        a, b = pair
        for op in '+-*/':
            if op == '+':
                news = [a + b]
            elif op == '*':
                news = [a * b]
            elif op == '-':
                news = [a - b, b - a]
            else:
                news = []
                if b != 0:
                    news.append(a / b)
                if a != 0:
                    news.append(b / a)

            for new in news:
                i = bisect.bisect(left, new)
                if i > 0:
                    temp = left[:i] + [new]
                else:
                    temp = [new]
                if i < n:
                    temp += left[i:]
                result = _judgePoint24_process(*temp)
                if result:
                    if op in {'-', '/'} and (
                            (len(news) == 2 and new == news[1])
                            or (len(news) == 1 and op == '/' and b == 0)):
                        result += ', {} {} {} = {}'.format(b, op, a, new)
                    else:
                        result += ', {} {} {} = {}'.format(a, op, b, new)
                    _cache_process[nums] = result
                    return result
    _cache_process[nums] = ''
    return ''


def print_24(nums):
    temp = _judgePoint24_process(*sorted(Fraction(i) for i in nums))
    for step in temp.split(', ')[::-1]:
        print(step)


print_24([4, 1, 8, 7])
print_24([3, 3, 7, 7])
print_24([1, 3, 4, 6])
print_24([-3, 10, 1, 1])

print_24([8, 1, 6, 6])
