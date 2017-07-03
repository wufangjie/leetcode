class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        acc = 0
        for elem in nums:
            acc ^= elem

        dif = 1
        while not acc & dif:
            dif <<= 1

        acc1 = acc2 = 0
        for elem in nums:
            if elem & dif:
                acc1 ^= elem
            else:
                acc2 ^= elem
        return [acc1, acc2]



print(Solution().singleNumber([1,2,1,3,2,5]))
