class Solution(object):
    def findDuplicates(self, nums):
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
                # print(nums)

        count = 0
        for i, elem in enumerate(nums):
            if elem < -1:
                nums[count] = i + 1
                count += 1
        return nums[:count]


print(Solution().findDuplicates([3, 8, 7, 6, 1, 5, 9, 1, 5, 3, 6, 7]))
print(Solution().findDuplicates([4,3,2,7,8,2,3,1]))
