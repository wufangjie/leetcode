# from itertools import zip_longest
from itertools import izip_longest


class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        l1, l2 = version1.split('.'), version2.split('.')
        for a, b in izip_longest(l1, l2, fillvalue='0'):
            a, b = int(a), int(b)
            if a > b:
                return 1
            elif a < b:
                return -1
        return 0
