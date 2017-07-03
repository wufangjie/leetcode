class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        n = len(nums)
        self.cumsum = [0] * (n + 1)
        for i in range(n):
            self.cumsum[i] = self.cumsum[i - 1] + nums[i]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.cumsum[j] - self.cumsum[i - 1]


    # def __init__(self, nums):
    #     """
    #     :type nums: List[int]
    #     """
    #     self._cache = {}
    #     self.nums = nums

    # def sumRange(self, i, j):
    #     """
    #     :type i: int
    #     :type j: int
    #     :rtype: int
    #     """
    #     if (i, j) not in self._cache:
    #         self._cache[i, j] = sum(self.nums[i:j+1])
    #     return self._cache[i, j]



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
