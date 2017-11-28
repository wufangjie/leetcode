import bisect


class MyCalendarThree(object):
    def __init__(self):
        self.pos = [float('-inf'), float('inf')]
        self.value = [0]
        self.k = 0

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: int
        """
        i = bisect.bisect_left(self.pos, start)
        if self.pos[i] != start:
            self.pos.insert(i, start)
            self.value.insert(i, self.value[i - 1])
        elif self.value[i] + 1 == self.value[i - 1]:
            self.pos.pop(i)
            self.value.pop(i - 1)
            i -= 1

        while True:
            self.value[i] += 1
            if self.k < self.value[i]:
                self.k = self.value[i]
            if end == self.pos[i + 1]:
                if self.value[i] == self.value[i + 1]:
                    self.pos.pop(i + 1)
                    self.value.pop(i + 1)
                break
            elif end < self.pos[i + 1]:
                self.pos.insert(i + 1, end)
                self.value.insert(i + 1, self.value[i] - 1)
                break
            i += 1

        return self.k




# Your MyCalendarThree object will be instantiated and called as such:
obj = MyCalendarThree()

# for s, e in [[10,20],[50,60],[10,40],[5,15],[5,10],[25,55]]:
#     print(obj.book(s, e))


for s, e in [[30,48],[57,70],[70,89],[6,19],[62,75],[3,13],[60,78],[66,77],[64,75],[93,100],[27,40],[93,100],[70,82],[45,57],[90,100],[42,59],[77,94],[14,30],[56,70],[8,22]]:
    print(obj.book(s, e))
