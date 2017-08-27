class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        pre1 = pre2 = float('-inf')
        modified = False
        for elem in nums:
            if elem < pre2:
                if modified:
                    return False

                if elem > pre1:
                    pre2 = elem
                else:
                    pre1 = pre2
                modified = True
            else:
                pre1, pre2 = pre2, elem

        return True

assert Solution().checkPossibility([4, 2, 3])
assert not Solution().checkPossibility([4, 2, 1])
