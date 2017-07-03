'''
Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new length.
'''


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur = 0
        for i, elem in enumerate(nums[2:]):
            if elem != nums[cur]:
                cur += 1
                nums[cur + 1] = elem
        return min(cur + 2, len(nums))


if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3]
    n = Solution().removeDuplicates(nums)
    print(nums[:n])
