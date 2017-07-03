# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

from collections import Iterable, deque

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.need_get_next = 1
        self.deque = deque([])
        self.g = iter(nestedList)


    def next(self, pop=True):
        """
        :rtype: int
        """
        if self.need_get_next:
            while True:
                while self.deque:
                    if self.deque[0].isInteger():
                    #if not isinstance(self.deque[0], Iterable):
                        break
                    else:
                        self.deque.extendleft(self.deque.popleft().getList()[::-1])
                else:
                    try:
                        self.deque.append(next(self.g))
                        continue
                    except:
                        pass
                break

        if pop:
            self.need_get_next = 1
            return self.deque.popleft().getInteger()
        else:
            self.need_get_next = 0


    def hasNext(self):
        """
        :rtype: bool
        """
        if self.need_get_next:
            self.next(pop=False)
        return bool(self.deque)


#[[1,1],2,[1,1]]
i, v = NestedIterator([1,[4,[6]]]), []
while i.hasNext():
    v.append(i.next())
print(v)

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
