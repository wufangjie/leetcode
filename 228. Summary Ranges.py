class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []

        start = nums[0]
        pre = start - 1
        result = []
        for elem in nums:
            if elem - pre == 1:
                pre = elem
            else:
                if start == pre:
                    result.append(str(start))
                else:
                    result.append('{}->{}'.format(start, pre))
                pre = start = elem
        if start == pre:
            result.append(str(start))
        else:
            result.append('{}->{}'.format(start, pre))
        return result


Solution().summaryRanges([0,1,2,4,5,7])
