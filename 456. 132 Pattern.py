from collections import deque
import bisect


class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        theMin, theMax = float('inf'), float('-inf')
        spans = deque([])

        for elem in nums:
            if elem < theMin:
                theMin = elem
            elif elem >= theMax:
                spans.clear()
                spans.appendleft((theMin, elem))
                theMax = elem
            elif elem <= spans[0][0]:
                spans.appendleft((theMin, elem))
            else:
                i = bisect.bisect_right(spans, (elem, theMax)) - 1
                if spans[i][0] == elem:
                    i -= 1
                elif spans[i][1] > elem:
                    return True

                for _ in range(i + 1):
                    spans.popleft()
                spans.appendleft((theMin, elem))
        return False


assert not Solution().find132pattern([1, 2, 3, 4])
assert Solution().find132pattern([3, 1, 4, 2])
assert Solution().find132pattern([-1, 3, 2, 0])
assert not Solution().find132pattern([3, 9, 2, 10, -9, -8, -7, -11, -10, -13, -12, -6])
