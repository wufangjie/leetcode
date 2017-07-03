from collections import defaultdict


class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        dct = defaultdict(int)
        for a in A:
            for b in B:
                dct[-a - b] += 1

        ret = 0
        for c in C:
            for d in D:
                if c + d in dct:
                    ret += dct[c + d]
        return ret
