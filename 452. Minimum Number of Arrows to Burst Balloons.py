# import heapq
import bisect


class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # NOTE: an one pass solution exist
        # the way I think is deleting the brust, but ignore them is far more better


        # actually heap is useless, so I use stack instead
        points.sort()
        starts = [p[0] for p in points]
        n = len(starts)
        seq = sorted(((p[1], i) for i, p in enumerate(points)), reverse=True)
        count = i = 0
        while seq:
            p, j = seq.pop()
            if j >= i:
                i = bisect.bisect_right(starts, p, lo=i)
                count += 1
                if i == n:
                    break
        return count

        # # TLE 35/43
        # points.sort(key=lambda x: x[1])
        # count = 0
        # while points:
        #     pos = points[0][1]
        #     points = [p for p in points if p[0] > pos]
        #     count += 1
        # return count

print(Solution().findMinArrowShots([[10,16], [2,8], [1,6], [7,12]]))
