'''
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:
Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

Example 2:
Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].
'''

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        def binary_search(array, lo, hi, target):
            while lo <= hi:
                mid = (lo + hi) >> 1
                if array[mid].start == target:
                    return mid
                elif array[mid].start > target:
                    return binary_search(array, lo, mid - 1, target)
                else:
                    return binary_search(array, mid + 1, hi, target)
            return lo

        maxlen = len(intervals)
        pos = binary_search(intervals, 0, maxlen - 1, newInterval.start)
        pos2 = binary_search(intervals, pos, maxlen - 1, newInterval.end)

        g = itertools.chain(
            intervals[max(0, pos - 1):pos], (newInterval,),
            intervals[max(0, pos2 - 1):pos2 + 1])
        result = [next(g)]
        for interval in g:
            if interval.start <= result[-1].end:
                if interval.end > result[-1].end:
                    result[-1].end = interval.end
            else:
                result.append(interval)
        return intervals[:max(0, pos - 1)] + result + intervals[pos2 + 1:]


if __name__ == '__main__':

    Interval.__repr__ = lambda x: '[{0.start}, {0.end}]'.format(x)
    intervals = [Interval(a, a + 2) for a in range(0, 20, 3)]
    xx = Solution().insert(intervals, Interval(-3, 18))
    xx = Solution().insert(intervals, Interval(8, 18))
    xx = Solution().insert(intervals, Interval(5.1, 5.2))
