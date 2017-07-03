class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 2:
            return n

        big, small = [], []
        for i in range(1, n):
            if nums[i] != nums[0]:
                if nums[i] > nums[0]:
                    big.append(nums[i])
                    small.append(nums[0])
                    current = 'small'
                else:
                    big.append(nums[0])
                    small.append(nums[1])
                    current = 'big'
                break

        else:
            return 1

        for i in range(i + 1, n):
            if current == 'big':
                if nums[i] < small[-1]:
                    small[-1] = nums[i]
                elif nums[i] > small[-1]:
                    big.append(nums[i])
                    current = 'small'
            else:
                if nums[i] > big[-1]:
                    big[-1] = nums[i]
                elif nums[i] < big[-1]:
                    small.append(nums[i])
                    current = 'big'
        return len(small) + len(big)


print(Solution().wiggleMaxLength([1,17,5,10,13,15,10,5,16,8]))
