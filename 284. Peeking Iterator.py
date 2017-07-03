class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self._peek = self._dummy = object()

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self._peek != self._dummy:
            return self._peek
        elif self.iterator.hasNext():
            self._peek = self.iterator.next()
            return self._peek
        raise StopIteration

    def next(self):
        """
        :rtype: int
        """
        ret = self.peek()
        self._peek = self._dummy
        return ret

    def hasNext(self):
        """
        :rtype: bool
        """
        if self._peek == self._dummy:
            return self.iterator.hasNext()
        else:
            return True

# I met Compile time limit exceeded the first time
