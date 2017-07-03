from collections import Counter


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # for k, v in Counter(nums):
        #     if v == 1:
        #         return k


        # easy to understand version
        # bit1 = bit2 = 0
        # for elem in nums:
        #     bit2 |= bit1 & elem
        #     bit1 ^= elem
        #     three = ~(bit1 & bit2) # which need to be set to 0
        #     bit1 &= three
        #     bit2 &= three
        # return bit1


        bit1 = bit2 = 0
        for elem in nums:
            bit1 = (bit1 ^ elem) & ~bit2
            bit2 = (bit2 ^ elem) & ~bit1

            # bit1 be 1 only if bit2 != 1 and bit1 ^ elem == 1
            # bit2 be 1 only if
            # ((bit2 == 1 and bit1 == elem == 0)
            #  or (bit2 == 0 and bit1 == elem == 1)) # the old bit1
            # as to new bit1, it's always 0, since bit1 == elem

        return bit1



print(Solution().singleNumber([1,4,3,3,4,4,3]))


# 二进制的题目都很难想到
# 思路是每个二进制位求和对三取余, 用两个变量来记录 mod 3 的余数
