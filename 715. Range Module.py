import bisect


class RangeModule(object):

    def __init__(self):
        self.lefts = [float('-inf'), float('inf')]
        self.rights = [float('-inf'), float('inf')]

    def addRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: void
        """
        i = bisect.bisect_right(self.lefts, left) - 1
        j = bisect.bisect_right(self.lefts, right, i)

        right = max(right, self.rights[j - 1])
        if self.rights[i] >= left:
            self.lefts = self.lefts[:i+1] + self.lefts[j:]
            self.rights = self.rights[:i] + [right] + self.rights[j:]
        else:
            self.lefts = self.lefts[:i+1] + [left] + self.lefts[j:]
            self.rights = self.rights[:i+1] + [right] + self.rights[j:]

    def queryRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: bool
        """
        i = bisect.bisect_right(self.lefts, left) - 1
        return right <= self.rights[i]

    def removeRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: void
        """
        i = bisect.bisect_right(self.lefts, left) - 1
        j = bisect.bisect_right(self.lefts, right, i)

        right_j_1 = self.rights[j - 1]
        if self.lefts[i] == left:
            i -= 1
        elif self.rights[i] > left:
            self.rights[i] = left

        if right < right_j_1:
            self.lefts = self.lefts[:i+1] + [right] + self.lefts[j:]
            self.rights = self.rights[:i+1] + [right_j_1] + self.rights[j:]
        else:
            self.lefts = self.lefts[:i+1] + self.lefts[j:]
            self.rights = self.rights[:i+1] + self.rights[j:]



obj = RangeModule()
obj.addRange(10, 20)
obj.removeRange(14, 16)
print(obj.queryRange(10, 14))
print(obj.queryRange(13, 15))
print(obj.queryRange(16, 17))
