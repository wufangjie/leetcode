class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        sumA = sum(A)
        theMax = current = sum([a * b for a, b in zip(range(n), A)])
        for i in range(n - 1, 0, -1):
            current += sumA - n * A[i]
            theMax = max(theMax, current)
        return theMax


print(Solution().maxRotateFunction([4, 3, 2, 6]))
