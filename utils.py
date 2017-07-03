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


class Node(object):
    def __init__(self, x):
        self.val = x

    __repr__ = __str__ = lambda self: '{}(val = {})'.format(
        self.__class__.__name__, self.val)


class ListNode(Node):
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class TreeNode(Node):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


# # some tips for binary search
# # I used lo <= hi in old codes, it's may not be elegant
# hi = len(seq) # not -1, or seq[-1] may not be compared
# while lo < hi:
#     mid = (lo + hi) >> 1
#     # ...
#     if some_condition:
#         lo = mid + 1 # always mid + 1, or may be endless loop
#     else:
#         hi = mid - 1 # may be just mid


class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    __repr__ = __str__ = lambda self: 'I[{}, {}]'.format(self.s, self.e)
