'''
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.
'''
# Definition for a point.
class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

from collections import defaultdict

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        point_dict = defaultdict(int)
        for p in points:
            point_dict[p.x, p.y] += 1

        if len(point_dict) < 2:
            return len(points)

        line, count, used = {}, {}, set()
        for i, (a2, b2) in enumerate(point_dict):
            left = used.copy()
            for (num, den), pts in line.iteritems():
            #for (num, den), pts in line.items():
                a1, b1 = next(iter(pts))
                if (a2 - a1) * den == (b2 - b1) * num:
                    pts.add((a2, b2))
                    left.difference_update(pts)
                    count[num, den] += point_dict[a2, b2]
                    if not left:
                        break

            for a1, b1 in left:
                num, den = (a2 - a1), (b2 - b1)
                line[num, den] = {(a1, b1), (a2, b2)}
                count[num, den] = point_dict[a1, b1] + point_dict[a2, b2]
            used.add((a2, b2))

        return max(count.values())


if __name__ == '__main__':
    temp = [[0,9],[138,429],[115,359],[115,359],[-30,-102],[230,709],[-150,-686],[-135,-613],[-60,-248],[-161,-481],[207,639],[23,79],[-230,-691],[-115,-341],[92,289],[60,336],[-105,-467],[135,701],[-90,-394],[-184,-551],[150,774]]
    p = [Point(a, b) for a, b in temp]
    assert Solution().maxPoints(p) == 12

    temp = [[3,10],[0,2],[0,2],[3,10]]
    p = [Point(a, b) for a, b in temp]
    assert Solution().maxPoints(p) == 4

    assert Solution().maxPoints([]) == 0

    temp = [0, 0], [0, 0]
    p = [Point(a, b) for a, b in temp]
    assert Solution().maxPoints(p) == 2
