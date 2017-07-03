class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # odd = set()
        # for n in nums:
        #     if n in odd:
        #         odd.remove(n)
        #     else:
        #         odd.add(n)
        # return odd.pop()

        # no extra version
        for n in nums[1:]:
            nums[0] ^= n
        return nums[0]
