class Solution(object):
    def findMinMoves(self, machines):
        """
        :type machines: List[int]
        :rtype: int
        """
        n = len(machines)
        theSum = sum(machines)
        if theSum % n != 0:
            return -1

        avg = theSum // n
        step = pre = 0
        for v in machines:
            pre += v - avg
            step = max(step, abs(pre), v - avg)
            # step = max(step, abs(pre))
            # if v > avg:
            #     step = max(step, v - avg)
        return step

# 流入有两边, 流出只有一边

assert Solution().findMinMoves([1,0,5]) == 3
assert Solution().findMinMoves([0,3,0]) == 2
assert Solution().findMinMoves([0,2,0]) == -1
assert Solution().findMinMoves([0,0,0,4]) == 3
assert Solution().findMinMoves([9,1,8,8,9]) == 4
