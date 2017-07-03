class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        if not buildings:
            return []

        result = [(buildings[0][0], 0)]
        for l, r, h in buildings:
            n = len(result)

            for hi in range(n-1, -1, -1):
                if result[hi][0] < r:
                    break

            for lo in range(hi, -1, -1):
                if result[lo][0] <= l:
                    break

            if l == result[lo][0]:
                mm = max(h, result[lo][1])
                if lo != 0 and result[lo - 1][1] == mm: # last but one case
                    temp = [(result[lo - 1][0], mm)]
                    lo -= 1
                else:
                    temp = [(l, mm)]
            else:
                temp = [result[lo]]
                if h > result[lo][1]:
                    temp.append((l, h))

            for i in range(lo + 1, hi + 1):
                mm = max(h, result[i][1])
                if temp[-1][1] != mm:
                    temp.append((result[i][0], mm))

            if hi == n - 1:
                temp.append((r, 0))
            else:
                if r != result[hi + 1][0] and temp[-1][1] != result[hi][1]:
                    temp.append((r, result[hi][1]))
            result = result[:lo] + temp + result[hi+1:]
        return result



assert Solution().getSkyline([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]) == [(2, 10), (3, 15), (7, 12), (12, 0), (15, 10), (20, 8), (24, 0)]
assert Solution().getSkyline([[2,9,10],[2,9,11]]) == [(2, 11), (9, 0)]
assert Solution().getSkyline([[2,9,10],[3,9,1]]) == [(2, 10), (9, 0)]
assert Solution().getSkyline([[0,2,3],[2,5,3]]) == [(0, 3), (5, 0)]
assert Solution().getSkyline([[3,7,8],[3,8,7],[3,9,6],[3,10,5],[3,11,4],[3,12,3],[3,13,2],[3,14,1]]) == [(3, 8), (7, 7), (8, 6), (9, 5), (10, 4), (11, 3), (12, 2), (13, 1), (14, 0)]
assert Solution().getSkyline([[3,10,20],[3,9,19],[3,8,18],[3,7,17],[3,6,16],[3,5,15],[3,4,14]]) == [(3, 20), (10, 0)]
