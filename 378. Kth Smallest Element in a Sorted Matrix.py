import heapq


class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        nrow, ncol = len(matrix), len(matrix[0])
        n = nrow * ncol
        inf = float('inf')

        if k <= (n >> 1) + 1:
            H = [-inf] * k
            m = min(k, ncol)
            H[-m:] = list(map(lambda x: -x, matrix[0][m-1 :: -1]))
            for i in range(1, nrow):
                for j in range(ncol):
                    if -matrix[i][j] > H[0]:
                        heapq.heapreplace(H, -matrix[i][j])
                    else:
                        break
            return -H[0]
        else:
            k = n + 1 - k
            H = [-inf] * k
            m = min(k, ncol)
            H[-m:] = matrix[-1][-m:]
            for i in range(nrow-2, -1, -1):
                for j in range(ncol-1, -1, -1):
                    if matrix[i][j] > H[0]:
                        heapq.heapreplace(H, matrix[i][j])
                    else:
                        break
            return H[0]

for k in range(1, 10):
    print(Solution().kthSmallest([[1,5,9],[10,11,13],[12,13,15]], k))
