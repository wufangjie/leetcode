'''
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
'''

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        def next_rec(i):
            if i == 0:
                nums.sort()
                return
            if nums[i] > nums[i - 1]:
                temp = sorted(nums[i - 1:])
                for j, _ in enumerate(temp):
                    if temp[j] > nums[i - 1]:
                        break
                nums[i - 1] = temp[j]
                nums[i:i + j] = temp[:j]
                nums[i + j:] = temp[j + 1:]
            else:
                next_rec(i - 1)
        next_rec(len(nums) - 1)


if __name__ == '__main__':
    assert Solution().nextPermutation([1, 2, 3, 7, 4, 6, 5])
