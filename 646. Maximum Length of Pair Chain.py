class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        pairs.sort(key=lambda x: x[1])
        pre = float('-inf')
        count = 0
        for p in pairs:
            if p[0] > pre:
                count += 1
                pre = p[1]
        return count
