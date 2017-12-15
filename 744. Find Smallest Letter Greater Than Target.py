class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        theMin, theMax = target, '{'
        for c in letters:
            if target < c < theMax:
                theMax = c
            elif c < theMin:
                theMin = c
        return theMin if theMax == '{' else theMax
