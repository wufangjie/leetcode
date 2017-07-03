'''
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?
'''


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        if n < 2:
            return
        for i in range(n >> 1):
            for j in range((n + 1) >> 1):
                matrix[i][j], matrix[j][n-i-1], matrix[n-i-1][n-j-1],\
                    matrix[n-j-1][i] = matrix[n-j-1][i], matrix[i][j],\
                                       matrix[j][n-i-1], matrix[n-i-1][n-j-1]


if __name__ == '__main__':
    matrix = [[1]]
    Solution().rotate(matrix)
    matrix = [[]]
    Solution().rotate(matrix)
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    Solution().rotate(matrix)
    matrix = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
    Solution().rotate(matrix)
