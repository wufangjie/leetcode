class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ca = cl = 0
        for c in s:
            if c == 'L':
                cl += 1
                if cl == 3:
                    return False
            else:
                if c == 'A':
                    ca += 1
                    if ca == 2:
                        return False
                cl = 0
        return True


# NOTE: two continuous 'L'
