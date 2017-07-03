'''
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
'''

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return intervals
        intervals = sorted(intervals, key=lambda x: x.start)
        result = intervals[:1]
        for interval in intervals[1:]:
            if interval.start <= result[-1].end:
                if interval.end > result[-1].end:
                    result[-1].end = interval.end
            else:
                result.append(interval)
        return result
