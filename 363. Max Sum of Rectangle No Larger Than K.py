import bisect


class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        if not matrix:
            return 0

        # use xrange get better performance
        target = k
        nrow, ncol = len(matrix), len(matrix[0])
        theMax = float('-inf')
        for j in range(ncol):
            acc = [0] * (j + 1)
            pre = [[] for _ in range(j + 1)]
            for i in range(nrow):
                new = 0
                for k in range(j, -1, -1):
                    new += matrix[i][k]
                    bisect.insort(pre[k], -acc[k])
                    pos = bisect.bisect_right(pre[k], target - acc[k] - new) - 1
                    if pos >= 0:
                        poss = pre[k][pos] + acc[k] + new
                        if poss == target:
                            return target
                        elif poss > theMax:
                            theMax = poss
                    acc[k] += new
        return 0 if theMax == float('-inf') else theMax


print(Solution().maxSumSubmatrix([[1,  0, 1], [0, -2, 3]], 2))
