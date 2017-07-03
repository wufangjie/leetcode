class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        stack = [0]
        theMax = 0
        for row in input.split('\n'):
            i = 0
            while row[i] == '\t':
                i += 1
            if '.' in row:
                theMax = max(theMax, stack[i] + len(row) - i)
            else:
                stack = stack[:i+1] + [stack[i] + len(row) - i + 1]
        return theMax


print(Solution().lengthLongestPath("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"))
