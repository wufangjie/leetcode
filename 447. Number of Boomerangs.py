from collections import defaultdict


class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        ret = 0
        for p in points:
            dist = defaultdict(int)
            for q in points:
                # if p != q: # much slower
                dist[(p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2] += 1
            ret += sum((i * (i - 1) for i in dist.values() if i > 1))
        return ret

# when
Solution().numberOfBoomerangs([[0,0],[1,0],[2,0]])
