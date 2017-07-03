class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        i = n = len(citations)
        citations = sorted(citations)
        while i > 0:
            if citations[-i] >= i:
                return i
            i -= 1
        return 0
