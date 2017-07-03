class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []

        nrow, ncol = len(matrix), len(matrix[0])
        result = [matrix[0][0]]
        from_top = True
        for theSum in range(1, nrow + ncol - 1):
            theMin = max(0, theSum - ncol + 1)
            theMax = min(nrow - 1, theSum)
            seq = (range(theMin, theMax + 1)
                   if from_top else range(theMax, theMin - 1, -1))
            for i in seq:
                result.append(matrix[i][theSum - i])
            from_top ^= True
        return result


print(Solution().findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]]))
