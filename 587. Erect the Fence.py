class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
    def __repr__(self):
        return 'Point({}, {})'.format(self.x, self.y)

    __str__ = __repr__


class Solution(object):
    def outerTrees(self, points):
        """
        :type points: List[Point]
        :rtype: List[Point]
        """
        n = len(points)
        points.sort(key=lambda p: (p.x, p.y))

        left_down = points[0]
        right = points[-1].x
        if left_down.x == right:
            return points

        i = 1
        while i < n:
            if points[i].x == left_down.x:
                i += 1
            else:
                ret = set(points[:i])
                break

        ixy = [(i, points[i - 1].x, points[i - 1].y),
               (i, left_down.x, left_down.y)]

        while ixy[0][1] < right or ixy[1][1] < right:
            idx = ixy[0] >= ixy[1]
            i, a, b = ixy[idx]
            sign = 1 if idx else -1
            num, den = sign * float('inf'), 1 # no add, last is ok

            for i in range(i, n):
                if points[i].x > a:
                    test = (den * (points[i].y - b)
                            - num * (points[i].x - a)) * sign * den # NOTE
                    if test < 0:
                        num, den = points[i].y - b, points[i].x - a
                        add, last = [points[i]], i
                    elif test == 0:
                        add.append(points[i])
                        last = i
            ret.update(add)
            ixy[idx] = last + 1, add[-1].x, add[-1].y
        ret.update(points[min(ixy[0][0], ixy[1][0]) : -1]) # right most line
        return list(ret)


print(Solution().outerTrees([Point(a, b) for a, b in [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]]))
print(Solution().outerTrees([Point(a, b) for a, b in [[1,1]]]))
print(Solution().outerTrees([Point(a, b) for a, b in [[1,2],[2,2],[4,2]]]), [[1,2],[2,2],[4,2]])
