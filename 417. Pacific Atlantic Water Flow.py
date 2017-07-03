from pprint import pprint

class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix:
            return []

        nrow, ncol = len(matrix), len(matrix[0])
        if nrow == 1:
            return [[0, j] for j in range(ncol)]
        elif ncol == 1:
            return [[i, 0] for i in range(nrow)]

        can = ([[[1, 0] for _ in range(ncol+1)]]
               + [[[0, 0] for _ in range(ncol+1)] for _ in range(1, nrow-1)]
               + [[[0, 1] for _ in range(ncol+1)]]
               + [[[1, 1] for _ in range(ncol+1)]])

        for i in range(nrow):
            can[i][0][0] = 1
            can[i][ncol-1][1] = 1
            can[i][ncol] = (1, 1)

        stack = ([(0, j) for j in range(1, ncol)]
                 + [(i, 0) for i in range(1, nrow)])
        while stack:
            i, j = stack.pop()
            for ii, jj in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                if not can[ii][jj][0] and matrix[ii][jj] >= matrix[i][j]:
                    can[ii][jj][0] = 1
                    stack.append((ii, jj))


        result = []
        stack = ([(nrow - 1, j) for j in range(ncol - 1)]
                 + [(i, ncol - 1) for i in range(nrow)])
        while stack:
            i, j = stack.pop()
            if can[i][j][0]:
                result.append([i, j])
            for ii, jj in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                if not can[ii][jj][1] and matrix[ii][jj] >= matrix[i][j]:
                    can[ii][jj][1] = 1
                    stack.append((ii, jj))
        return result




# 一开始不太明白题目的意思, 就是说哪些点的水既能流进太平洋, 又能流进大西洋


# print(Solution().pacificAtlantic([[1,5,2,2,3],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))

# print(Solution().pacificAtlantic([[8,12,0,17,8,7,7,1,12,19,12,19,14,1,16,0,14,7,4,14,14,8,17,18,9,14,19,16,19,17,7,14,13,17,2,11,16,8,8,8]]))

print(Solution().pacificAtlantic([[1,2],[4,3]]))
