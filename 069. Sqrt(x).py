'''
Implement int sqrt(int x).

Compute and return the square root of x.
'''

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        f = lambda y: y * y - x
        neg, pos = 0, x
        while int(neg) != int(pos):
            mid = (neg + pos) / 2.
            if f(mid) == 0:
                return int(mid)
            elif f(mid) > 0:
                pos = mid
            else:
                neg = mid
        return int(neg)
