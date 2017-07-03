# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


class SummaryRanges(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.count = {}
        self.interval = {}
        self.disjoint = {}

    def addNum(self, val):
        """
        :type val: int
        :rtype: void
        """
        if val not in self.disjoint:
            if val - 1 in self.disjoint and val + 1 in self.disjoint:
                i = self.get_parent(val - 1)
                j = self.get_parent(val + 1)
                if self.count[i] < self.count[j]:
                    self.count[j] += self.count[i] + 1
                    self.disjoint[val] = self.disjoint[i] = j
                    self.interval[j].start = self.interval[i].start
                    self.interval.pop(i)
                else:
                    self.count[i] += self.count[j] + 1
                    self.disjoint[val] = self.disjoint[j] = i
                    self.interval[i].end = self.interval[j].end
                    self.interval.pop(j)
            elif val - 1 in self.disjoint:
                self.disjoint[val] = i = self.get_parent(val - 1)
                self.count[i] += 1
                self.interval[i].end = val
            elif val + 1 in self.disjoint:
                self.disjoint[val] = j = self.get_parent(val + 1)
                self.count[j] += 1
                self.interval[j].start = val
            else:
                self.disjoint[val] = val
                self.count[val] = 1
                self.interval[val] = Interval(val, val)

    def getIntervals(self):
        """
        :rtype: List[Interval]
        """
        # increasing and key
        return sorted(self.interval.values(), key=lambda x: x.start)

    def get_parent(self, val):
        if self.disjoint[val] == val:
            return val
        else:
            self.disjoint[val] = self.get_parent(self.disjoint[val])
            return self.disjoint[val]




# # Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# for val in [1, 3, 7, 2, 6, 5, 4]:
#     obj.addNum(val)
#     print(obj.getIntervals())


    ["SummaryRanges","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals"] [[],[6],[],[6],[],[0],[],[4],[],[8],[],[7],[],[6],[],[4],[],[7],[],[5],[]]


obj = SummaryRanges()
for val in [6, 6, 0, 4, 8, 7, 6, 4, 7, 5]:
    obj.addNum(val)
    print(obj.getIntervals())
[null,null,[[6,6]],null,[[6,6]],null,[[0,0],[6,6]],null,[[0,0],[4,4],[6,6]],null,[[0,0],[8,8],[4,4],[6,6]],null,[[0,0],[4,4],[6,8]],null,[[0,0],[4,4],[6,8]],null,[[0,0],[4,4],[6,8]],null,[[0,0],[4,4],[6,8]],null,[[0,0],[4,8]]]

[null,null,[[6,6]],null,[[6,6]],null,[[0,0],[6,6]],null,[[0,0],[4,4],[6,6]],null,[[0,0],[4,4],[6,6],[8,8]],null,[[0,0],[4,4],[6,8]],null,[[0,0],[4,4],[6,8]],null,[[0,0],[4,4],[6,8]],null,[[0,0],[4,4],[6,8]],null,[[0,0],[4,8]]]
