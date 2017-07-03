'''
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

You should return [1,2,3,6,9,8,7,4,5].
'''

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return matrix
        m, n = len(matrix), len(matrix[0])
        theMin = min(m, n)
        max_valid_layer = (theMin - 1) >> 1
        def spiral_rec(layer):
            for i in range(layer, n - layer):
                yield matrix[layer][i]
            for i in range(layer + 1, m - layer):
                yield matrix[i][n - layer - 1]
            if layer == max_valid_layer and theMin & 1:
                return
            for i in range(n - layer - 2, layer - 1, -1):
                yield matrix[m - layer - 1][i]
            for i in range(m - layer - 2, layer, -1):
                yield matrix[i][layer]
            if layer == max_valid_layer and not (theMin & 1):
                return
            for elem in spiral_rec(layer + 1):
                yield elem
        return list(spiral_rec(0))


if __name__ == '__main__':
    import numpy as np
    aa = np.arange(20).reshape(4, 5)
    print(Solution().spiralOrder(aa.tolist()))
    Solution().spiralOrder([[2, 3]])

    assert Solution().spiralOrder(np.arange(24).reshape(4, 6).tolist()) ==\
        [0, 1, 2, 3, 4, 5, 11, 17, 23, 22, 21, 20, 19, 18, 12, 6, 7, 8, 9, 10, 16, 15, 14, 13]
    assert Solution().spiralOrder(np.arange(24).reshape(3, 8).tolist()) ==\
        [0, 1, 2, 3, 4, 5, 6, 7, 15, 23, 22, 21, 20, 19, 18, 17, 16, 8, 9, 10, 11, 12, 13, 14]
    assert Solution().spiralOrder(np.arange(24).reshape(6, 4).tolist()) ==\
        [0, 1, 2, 3, 7, 11, 15, 19, 23, 22, 21, 20, 16, 12, 8, 4, 5, 6, 10, 14, 18, 17, 13, 9]
    assert Solution().spiralOrder(np.arange(24).reshape(8, 3).tolist()) ==\
        [0, 1, 2, 5, 8, 11, 14, 17, 20, 23, 22, 21, 18, 15, 12, 9, 6, 3, 4, 7, 10, 13, 16, 19]
