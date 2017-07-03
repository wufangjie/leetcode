from collections import deque


class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = deque([])
        self.dummy = object()

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.stack.append(self.dummy)
        self.stack.append(x)
        while self.stack[0] != self.dummy:
            self.stack.append(self.stack.popleft())
        self.stack.popleft()

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self.stack.popleft()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.stack[0]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return not bool(self.stack)



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
