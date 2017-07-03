import bisect


class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []


    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        bisect.insort_right(self.nums, num)


    def findMedian(self):
        """
        :rtype: float
        """
        n = len(self.nums)
        mid = n >> 1
        if n & 1:
            return self.nums[mid]
        else:
            return (self.nums[mid] + self.nums[mid-1]) / 2.




# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
