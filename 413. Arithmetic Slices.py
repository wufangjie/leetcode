class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        if n < 3:
            return 0

        diff = A[1] - A[0]
        ret = count = 0
        for i in range(2, n):
            if A[i] - A[i - 1] == diff:
                count += 1
            else:
                if count:
                    ret += (count + 1) * (count) // 2
                    count = 0
                diff = A[i] - A[i - 1]

        return ret + (count + 1) * (count) // 2
