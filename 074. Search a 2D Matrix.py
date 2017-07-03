'''
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

    Integers in each row are sorted from left to right.
    The first integer of each row is greater than the last integer of the previous row.

For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]

Given target = 3, return true.
'''

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False

        nrow, ncol = len(matrix), len(matrix[0])
        for i in range(nrow):
            if matrix[i][-1] >= target:
                break
        else:
            return False
        for j in range(ncol - 1, -1, -1):
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                return False
        return False


if __name__ == '__main__':
    Solution().searchMatrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], 3)
