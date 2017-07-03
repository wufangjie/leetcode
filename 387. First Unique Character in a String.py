class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        visited = set()
        for i, elem in enumerate(s):
            if elem not in visited:
                if not s.count(elem, i+1):
                    return i
                visited.add(elem)
        return -1
