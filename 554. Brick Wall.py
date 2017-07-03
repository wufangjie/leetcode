import heapq


class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        nrow = len(wall)
        H = [(wall[i][0], i, 1) for i in range(nrow)]
        right_most = sum(wall[0])
        heapq.heapify(H)

        theMax = 0
        while H:
            left_most = H[0][0]
            if left_most == right_most:
                return nrow - theMax

            count = 0
            while H[0][0] == left_most:
                _, i, j = H[0]
                heapq.heapreplace(H, (left_most + wall[i][j], i, j + 1))
                count += 1
            if count == nrow:
                return 0
            else:
                theMax = max(theMax, count)




print(Solution().leastBricks([[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]))
