class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        if not timeSeries:
            return 0
        pre = timeSeries[0]
        ret = duration
        for t in timeSeries:
            ret += min(t - pre, duration)
            pre = t
        return ret
