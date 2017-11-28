class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        if image[sr][sc] == newColor:
            return image
        ret = [row[:] for row in image]
        oldColor = ret[sr][sc]
        nrow, ncol = len(image), len(image[0])
        to_paint = {(sr, sc)}
        while to_paint:
            i, j = to_paint.pop()
            ret[i][j] = newColor
            for ii, jj in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= ii < nrow and 0 <= jj < ncol:
                    if image[ii][jj] == oldColor and ret[ii][jj] != newColor:
                        to_paint.add((ii, jj))
        return ret


print(Solution().floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2))
