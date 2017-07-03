class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        n = len(nums) * len(nums[0])
        if n != r * c or r == len(nums):
            return nums
        else:
            vec = []
            for row in nums:
                vec.extend(row)
            return [vec[i:i+c] for i in range(0, n, c)]
