# 好题

inf = float('inf')

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = [(None, inf)]

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append((x, min(x, self.stack[-1][1])))

    def pop(self):
        """
        :rtype: void
        """
        if self.stack[-1][1] != inf:
            self.stack.pop()


    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack[-1][1]
