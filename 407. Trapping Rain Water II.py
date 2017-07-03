import heapq
from copy import deepcopy


class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        if not heightMap:
            return 0

        nrow, ncol = len(heightMap), len(heightMap[0])
        maxMap = deepcopy(heightMap)

        for i in range(1, nrow - 1):
            for j in range(1, ncol - 1):
                maxMap[i][j] = max(
                    heightMap[i][j], min(maxMap[i][j - 1], maxMap[i - 1][j]))

            for j in range(ncol - 2, 0, -1):
                if maxMap[i][j] > maxMap[i][j + 1]:
                    maxMap[i][j] = max(heightMap[i][j], maxMap[i][j + 1])

        for j in range(ncol - 2, 0, -1):
            for i in range(nrow - 2, 0, -1):
                if maxMap[i][j] > maxMap[i + 1][j]:
                    maxMap[i][j] = max(heightMap[i][j], maxMap[i + 1][j])

        used, left = set(), set()
        for i in range(1, nrow - 1):
            for j in range(1, ncol - 1):
                if maxMap[i][j] > heightMap[i][j]:
                    left.add((i, j))
                else:
                    used.add((i, j))

        while used:
            i, j = used.pop()
            h = heightMap[i][j]
            for ii, jj in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                if (ii, jj) in left and maxMap[ii][jj] > h:
                    if heightMap[ii][jj] <= h:
                        maxMap[ii][jj] = h
                    else:
                        # maxMap[ii][jj] = heightMap[ii][jj]
                        left.remove((ii, jj))
                        used.add((ii, jj))

        H = [(maxMap[i][j], i, j) for i, j in left]
        heapq.heapify(H)

        theSum = 0
        while left:
            h, i, j = heapq.heappop(H)
            if h == maxMap[i][j]:
                # print('i={}, j={}, max={}, h={}, add={}'.format(
                #     i, j, h, heightMap[i][j], h - heightMap[i][j]))
                theSum += h - heightMap[i][j]
                left.remove((i, j))
                for ii, jj in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                    if ((ii, jj) in left and maxMap[ii][jj] > h
                        and maxMap[ii][jj] > heightMap[ii][jj]):
                        maxMap[ii][jj] = max(h, heightMap[ii][jj])
                        heapq.heappush(H, (maxMap[ii][jj], ii, jj))

        return theSum


print(Solution().trapRainWater([]))
print(Solution().trapRainWater([[1]]))

assert Solution().trapRainWater(
    [[9, 4, 3, 4, 9, 9],
     [9, 4, 1, 4, 9, 9],
     [9, 3, 9, 9, 9, 9],
     [9, 7, 8, 2, 8, 2],
     [9, 5, 9, 9, 9, 9],
     [9, 9, 9, 9, 9, 9]]) == 11

assert Solution().trapRainWater(
    [[8, 3, 7, 4, 6, 7, 7, 5, 6, 9],
     [4, 8, 9, 7, 3, 3, 7, 6, 4, 2],
     [4, 5, 4, 5, 6, 6, 3, 1, 6, 7],
     [9, 4, 3, 3, 3, 2, 4, 3, 6, 6],
     [7, 5, 3, 4, 6, 3, 9, 8, 2, 4],
     [7, 4, 2, 8, 1, 6, 5, 4, 5, 2],
     [2, 9, 6, 6, 8, 1, 4, 2, 8, 2],
     [8, 2, 8, 5, 1, 7, 4, 9, 5, 6],
     [5, 7, 8, 1, 7, 9, 6, 4, 5, 3],
     [4, 2, 3, 7, 5, 3, 1, 8, 1, 6]]) == 69

assert Solution().trapRainWater(
    [[1,4,3,1,3,2],
     [3,2,1,3,2,4],
     [2,3,3,2,3,1]]) == 4

assert Solution().trapRainWater([[54, 55, 19, 99, 28, 11, 65, 7, 94, 55, 41, 26, 18, 50, 62, 65, 99, 21, 50, 74], [65, 11, 15, 3, 24, 92, 91, 4, 52, 78, 22, 99, 22, 21, 68, 8, 32, 83, 88, 94], [10, 84, 55, 38, 52, 45, 64, 9, 17, 65, 42, 34, 99, 76, 10, 73, 35, 99, 29, 73], [54, 50, 4, 54, 18, 94, 70, 97, 57, 88, 50, 11, 40, 11, 76, 19, 19, 44, 10, 34], [27, 86, 64, 62, 29, 85, 15, 40, 8, 8, 24, 44, 43, 20, 96, 41, 62, 61, 61, 52], [84, 22, 83, 58, 22, 40, 96, 85, 25, 6, 31, 35, 21, 28, 16, 43, 89, 36, 99, 98], [30, 77, 56, 13, 77, 95, 54, 97, 56, 64, 15, 93, 23, 99, 86, 74, 72, 24, 32, 57], [47, 56, 12, 34, 57, 47, 99, 73, 29, 31, 56, 80, 13, 23, 40, 19, 52, 69, 73, 96], [36, 33, 27, 26, 54, 29, 22, 58, 14, 43, 22, 32, 66, 45, 10, 39, 87, 41, 89, 92], [72, 38, 60, 11, 9, 62, 93, 96, 57, 45, 46, 24, 80, 29, 88, 68, 32, 37, 94, 6], [70, 65, 78, 8, 20, 8, 45, 86, 28, 27, 76, 98, 41, 48, 54, 67, 91, 18, 83, 83], [78, 98, 87, 34, 86, 24, 56, 26, 16, 48, 11, 13, 5, 32, 11, 51, 51, 4, 98, 15], [15, 27, 29, 70, 26, 56, 13, 9, 52, 50, 83, 32, 86, 71, 80, 66, 24, 74, 3, 63], [8, 32, 85, 75, 45, 42, 7, 17, 14, 93, 44, 51, 16, 2, 7, 33, 59, 97, 93, 28], [65, 53, 99, 75, 36, 59, 11, 76, 75, 93, 75, 22, 5, 71, 51, 39, 32, 78, 61, 8], [48, 93, 97, 95, 26, 84, 86, 14, 33, 69, 90, 2, 3, 62, 9, 9, 5, 24, 88, 82], [81, 78, 22, 80, 27, 16, 70, 92, 79, 70, 95, 68, 58, 62, 61, 8, 19, 11, 45, 80], [52, 49, 10, 66, 92, 1, 80, 78, 73, 71, 42, 33, 51, 33, 32, 59, 93, 74, 44, 23], [91, 13, 7, 98, 75, 85, 94, 60, 80, 58, 90, 7, 38, 50, 89, 74, 69, 47, 2, 83], [10, 15, 81, 43, 6, 34, 43, 85, 13, 84, 97, 66, 69, 41, 32, 59, 46, 74, 94, 55]]) == 3212


# from pprint import pprint
# import numpy as np
# print(np.random.randint(1, 10, (10, 10)).tolist())



        # seq = sorted([(heightMap[i][j], i, j)
        #               for i in range(1, nrow - 1) for j in range(1, ncol - 1)])
        # realMap = deepcopy(heightMap)
        # inf = float('inf')
        # maxMap = [[inf] * ncol for _ in range(nrow)]

        # idct, jdct = {0: 1, nrow - 1: nrow - 2}, {0: 1, ncol - 1: ncol - 2}


        # def dfs_sum(i, j, h, visited, dealt):
        #     h = min(h, maxMap[i][j])
        #     if dealt and h <= realMap[i][j]: # first time
        #         return 0
        #     dealt.add((i, j))
        #     acc = h - realMap[i][j]
        #     realMap[i][j] = h
        #     for ij in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
        #         if ij not in dealt and ij in visited:
        #             acc += dfs_sum(ij[0], ij[1], h, visited, dealt)
        #     return acc

        # def dfs_res(i, j, h, visited, dealt):
        #     if h < maxMap[i][j]:
        #         h = max(h, realMap[i][j])
        #         maxMap[i][j] = h
        #         dealt.add((i, j))
        #         for ij in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
        #             if ij not in dealt and ij in visited:
        #                 dfs_res(ij[0], ij[1], h, visited, dealt)

        # theSum = 0
        # used = set()

        # for h, i, j in seq:
        #     if (i, j) in used:
        #         continue
        #     visited = {(i, j)}
        #     H = [(h, i, j)]
        #     while H:
        #         h, i, j = heapq.heappop(H)
        #         # if h == 7:
        #         #     import pdb
        #         #     pdb.set_trace()

        #         theSum += dfs_sum(i, j, h, visited, set())

        #         if i == 0 or i == nrow - 1 or j == 0 or j == ncol - 1:
        #             ii, jj = idct.get(i, i), jdct.get(j, j)
        #             h = max(realMap[i][j], realMap[ii][jj])
        #             dfs_res(ii, jj, h, visited, set())
        #         else:
        #             for ii, jj in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
        #                 if (ii, jj) in used:
        #                     h = max(realMap[ii][jj], realMap[i][j])
        #                     dfs_res(ii, jj, h, visited, dealt)
        #                 elif (ii, jj) not in visited:
        #                     heapq.heappush(H, (realMap[ii][jj], ii, jj))
        #                     visited.add((ii, jj))

        #     used.update(visited)
        # return theSum
