from typing import List
import heapq

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        buildings.sort(key=lambda lst: (lst[0], -lst[2], lst[1]))
        heap = [[0, -2 ** 31]]
        ret = []
        for (x, x2, y) in buildings:
            self.pop_until(ret, heap, x)
            if y > -heap[0][0]:
                ret.append([x, y])
                heapq.heappush(heap, [-y, -x2])
            elif y == -heap[0][0]:
                if x2 > -heap[0][1]:
                    heap[0][1] = -x2
            elif x2 > -heap[0][1]:
                heapq.heappush(heap, [-y, -x2])
        self.pop_until(ret, heap, 2 ** 31)
        return ret

    @staticmethod
    def pop_until(ret: List[List[int]], heap: List[List[int]], x: int):
        while -heap[0][1] < x:
            height, right = heapq.heappop(heap)
            if ret and ret[-1][1] is None:
                if -right > ret[-1][0]:
                    ret[-1][1] = -height
                    ret.append([-right, None])
            else:
                ret.append([-right, None]) # -right for same height
        if ret and ret[-1][1] is None:
            ret[-1][1] = -heap[0][0]




assert Solution().getSkyline([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]) == [(2, 10), (3, 15), (7, 12), (12, 0), (15, 10), (20, 8), (24, 0)]
assert Solution().getSkyline([[2,9,10],[2,9,11]]) == [(2, 11), (9, 0)]
assert Solution().getSkyline([[2,9,10],[3,9,1]]) == [(2, 10), (9, 0)]
assert Solution().getSkyline([[0,2,3],[2,5,3]]) == [(0, 3), (5, 0)]
assert Solution().getSkyline([[3,7,8],[3,8,7],[3,9,6],[3,10,5],[3,11,4],[3,12,3],[3,13,2],[3,14,1]]) == [(3, 8), (7, 7), (8, 6), (9, 5), (10, 4), (11, 3), (12, 2), (13, 1), (14, 0)]
assert Solution().getSkyline([[3,10,20],[3,9,19],[3,8,18],[3,7,17],[3,6,16],[3,5,15],[3,4,14]]) == [(3, 20), (10, 0)]
