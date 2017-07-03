class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        if not M:
            return 0

        count, n = 0, len(M)
        rowSum = {i: sum(row) for i, row in enumerate(M)}
        while rowSum:
            i = max(rowSum.keys(), key=lambda x: rowSum[x])
            if rowSum[i] == 1:
                return count + len(rowSum)

            to_pop = {i}
            while to_pop:
                i = to_pop.pop()
                rowSum.pop(i)
                for j in rowSum:
                    if M[i][j] == 1:
                        to_pop.add(j)

            count += 1
        return count


print(Solution().findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))
print(Solution().findCircleNum([[1,1,0],[1,1,1],[0,1,1]]))
