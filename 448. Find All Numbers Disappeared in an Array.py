class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def update(i):
            if nums[i - 1] <= 0:
                nums[i - 1] -= 1
            else:
                j = nums[i - 1]
                nums[i - 1] = -1
                update(j)

        for i, elem in enumerate(nums):
            if elem > 0:
                nums[i] = 0
                update(elem)

        count = 0
        for i, elem in enumerate(nums):
            if elem == 0:
                nums[count] = i + 1
                count += 1
        return nums[:count]
