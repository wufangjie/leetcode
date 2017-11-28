import bisect


class MyCalendarTwo(object):
    def __init__(self):
        self.pos = [float('-inf'), float('inf')]
        self.value = [0]

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        i = bisect.bisect_right(self.pos, start) - 1
        j = bisect.bisect_left(self.pos, end, lo=i)
        if max(self.value[i:j]) == 2:
            return False

        if self.pos[i] != start:
            i += 1
            self.pos.insert(i, start)
            self.value.insert(i, self.value[i - 1])
        elif self.value[i] + 1 == self.value[i - 1]:
            self.pos.pop(i)
            self.value.pop(i - 1)
            i -= 1

        while True:
            self.value[i] += 1
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

        return True



obj = MyCalendarTwo()
for s, e in [(10, 20), (50, 60), (10, 40), (5, 15), (5, 10), (25, 55)]:
    print(obj.book(s, e))
