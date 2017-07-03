'''
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.
'''

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return matrix
        row0, col0 = set(), set()
        nrow, ncol = len(matrix), len(matrix[0])
        for i, rows in enumerate(matrix):
            for j, elem in enumerate(rows):
                if elem == 0:
                    row0.add(i)
                    col0.add(j)
        for i in row0:
            for j in range(ncol):
                matrix[i][j] = 0
        for j in col0:
            for i in range(nrow):
                matrix[i][j] = 0


if __name__ == '__main__':
    matrix = []
    Solution().setZeroes(matrix)
    print(matrix)
