class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        import pdb;pdb.set_trace()
        if not M:
            return M
        nrow, ncol = len(M), len(M[0])
        if ncol == 1:
            if nrow == 1:
                return M
            else:
                temp = self.sum_row([row[0] for row in M], nrow)
                return [[v // (3 if 0 < j < nrow - 1 else 2)]
                        for j, v in enumerate(temp)]
        else:
            rows = [self.sum_row(row, ncol) for row in M]

        if nrow == 1:
            return [[rows[0][j] // (3 if 0 < j < ncol - 1 else 2)
                     for j in range(ncol)]]
        ret = []

        for i, row in enumerate(M):
            if i == 0:
                ret.append([(rows[i][j] + rows[i + 1][j])
                            // (6 if 0 < j < ncol - 1 else 4)
                            for j in range(ncol)])
            elif i == nrow - 1:
                ret.append([(rows[i - 1][j] + rows[i][j])
                            // (6 if 0 < j < ncol - 1 else 4)
                            for j in range(ncol)])
            else:
                ret.append([(rows[i - 1][j] + rows[i][j] + rows[i + 1][j])
                            // (9 if 0 < j < ncol - 1 else 6)
                            for j in range(ncol)])
        return ret

    @staticmethod
    def sum_row(row, ncol):
        if ncol < 2:
            return row

        ret = [row[0] + row[1]]
        if ncol == 2:
            return ret * 2

        ret.append(ret[0] + row[2])

        for i in range(3, ncol):
            ret.append(ret[-1] + row[i] - row[i - 3])

        ret.append(row[-1] + row[-2])
        return ret


# print(Solution().imageSmoother([[255,1,1],[1,0,1],[1,1,39]]))

# print(Solution().imageSmoother([[255,1]]))

# print(Solution().imageSmoother([[1]]))
# print(Solution().imageSmoother([[2, 3]]))

# print(Solution().imageSmoother([[3],[2]]))

print(Solution().imageSmoother([[7],[9],[6]]))
