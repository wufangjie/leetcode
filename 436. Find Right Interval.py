from utils import Interval


class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        """
        n = len(intervals)
        start = sorted([(v.start, i) for i, v in enumerate(intervals)])
        end = sorted([(v.end, i) for i, v in enumerate(intervals)])
        i = j = 0
        result = [-1] * n
        while i < n:
            if start[i][0] >= end[j][0]:
                result[end[j][1]] = start[i][1]
                j += 1
            else:
                i += 1
        return result
