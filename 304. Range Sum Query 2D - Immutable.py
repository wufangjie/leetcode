class NumMatrix(object):
    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if not matrix:
            return
        nrow, ncol = len(matrix), len(matrix[0])
        self.cumsum = [[0] * (ncol + 1) for _ in range(nrow + 1)]
        for i in range(nrow):
            for j in range(ncol):
                self.cumsum[i][j] = (matrix[i][j]
                                     + self.cumsum[i-1][j]
                                     + self.cumsum[i][j-1]
                                     - self.cumsum[i-1][j-1])

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return (self.cumsum[row2][col2] - self.cumsum[row2][col1-1]
                - self.cumsum[row1-1][col2] + self.cumsum[row1-1][col1-1])



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)


obj = NumMatrix([[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]])
for param in [2,1,4,3],[1,1,2,2],[1,2,2,4]:
    print(obj.sumRegion(*param))


obj = NumMatrix([[]])


[[[[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]],[2,1,4,3],[1,1,2,2],[1,2,2,4]]
