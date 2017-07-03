from collections import defaultdict


class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        seq_by_last = defaultdict(set)
        for elem in nums:
            new = {(elem,)}
            for k, v in seq_by_last.items():
                if elem >= k:
                    for val in v:
                        new.add(tuple(list(val) + [elem]))
            seq_by_last[elem].update(new)
        return [list(val) for v in seq_by_last.values()
                for val in v if len(val) > 1]


print(Solution().findSubsequences([4,6,7,7,7]))
