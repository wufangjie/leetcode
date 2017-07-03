'''
Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

For example,
Given n = 3,
You should return the following matrix:

[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
'''


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n < 1:
            return []
        matrix = {}
        theMin = m = n
        max_valid_layer = (theMin - 1) >> 1
        def spiral_rec(layer=0, cur=1):
            for i in range(layer, n - layer):
                matrix[layer, i] = cur
                cur += 1
            for i in range(layer + 1, m - layer):
                matrix[i, n - layer - 1] = cur
                cur += 1
            if layer == max_valid_layer and theMin & 1:
                return
            for i in range(n - layer - 2, layer - 1, -1):
                matrix[m - layer - 1, i] = cur
                cur += 1
            for i in range(m - layer - 2, layer, -1):
                matrix[i, layer] = cur
                cur += 1
            if layer == max_valid_layer and not (theMin & 1):
                return
            spiral_rec(layer + 1, cur)
        spiral_rec()
        return [[matrix[i, j] for j in range(n)] for i in range(m)]


if __name__ == '__main__':
    print(Solution().generateMatrix(3))
    print(Solution().generateMatrix(4))
    print(Solution().generateMatrix(5))
    print(Solution().generateMatrix(1))
