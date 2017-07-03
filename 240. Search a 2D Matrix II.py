class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False

        nrow = len(matrix)
        r, c = 0, len(matrix[0]) - 1
        while c > -1 and r < nrow:
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                r += 1
            else:
                c -= 1
        return False

        # def find(l, r, u, d):
        #     if l > r or u > d:
        #         return False

        #     mid_h = (l + r) >> 1
        #     mid_v = (u + d) >> 1
        #     if matrix[mid_v][mid_h] == target:
        #         return True
        #     elif matrix[mid_v][mid_h] > target:
        #         return (find(mid_h, r, u, mid_v-1)
        #                 or find(l, mid_h-1, mid_v, d)
        #                 or find(l, mid_h-1, u, mid_v-1))
        #     else:
        #         return (find(mid_h+1, r, u, mid_v)
        #                 or find(l, mid_h, mid_v+1, d)
        #                 or find(mid_h+1, r, mid_v+1, d))

        # return find(0, len(matrix[0])-1, 0, len(matrix)-1)




# Solution().searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 5)

# Solution().searchMatrix([[1, 1]], 2)


Solution().searchMatrix([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]], 5)
