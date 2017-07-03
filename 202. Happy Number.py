class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        met = set()
        while n != 1:
            if n in met:
                return False
            met.add(n)
            n = sum(map(lambda x: int(x) ** 2, str(n)))
        return True
