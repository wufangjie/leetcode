class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        tp = sorted(map(lambda x: int(x[:2]) * 60 + int(x[3:]), timePoints))
        theMin = tp[0] + 1440 - tp[-1]
        for i in range(len(tp) - 1):
            theMin = min(theMin, tp[i + 1] - tp[i])
        return theMin
