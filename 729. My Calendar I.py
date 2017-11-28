import bisect


class MyCalendar(object):
    def __init__(self):
        self.start = [float('-inf'), float('inf')]
        self.end = [float('-inf'), float('inf')]

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        i = bisect.bisect_right(self.end, start)
        if self.start[i] >= end:
            if self.end[i - 1] == start:
                if self.start[i] == end:
                    self.start.pop(i)
                    self.end.pop(i - 1)
                else:
                    self.end[i - 1] = end
            elif self.start[i] == end:
                self.start[i] = start
            else:
                self.start.insert(i, start)
                self.end.insert(i, end)
            return True
        return False


obj = MyCalendar()
print(obj.book(10, 20))
print(obj.book(15, 25))
print(obj.book(20, 30))







# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
