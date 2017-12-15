import heapq


class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        time_table = [[-1] * N for _ in range(N)]
        for u, v, w in times:
            time_table[u - 1][v - 1] = w

        H = [(0, K - 1)]
        received = set()
        while H:
            w0, u = heapq.heappop(H)
            if u not in received:
                ret = w0
                received.add(u)
                for v, w in enumerate(time_table[u]):
                    if w != -1 and v not in received:
                        heapq.heappush(H, (w + w0, v))
        if len(received) != N:
            return -1
        return ret


# print(Solution().networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2))


# NOTE: the description says 1 <= w <= 100, actually not


print(Solution().networkDelayTime([[3,5,78],[2,1,1],[1,3,0],[4,3,59],[5,3,85],[5,2,22],[2,4,23],[1,4,43],[4,5,75],[5,1,15],[1,5,91],[4,1,16],[3,2,98],[3,4,22],[5,4,31],[1,2,0],[2,5,4],[4,2,51],[3,1,36],[2,3,59]], 5, 5))
