class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self._cache = {}
        self.nums = nums

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        self.nums[i] = val
        self._cache.clear()

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if (i, j) not in self._cache:
            self._cache[i, j] = sum(self.nums[i:j+1])
        return self._cache[i, j]




# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
