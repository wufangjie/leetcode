import bisect


class LogSystem(object):
    def __init__(self):
        self.seq = []
        self.gra = {
            'Year': 1, 'Month': 2, 'Day': 3, 'Hour': 4, 'Minute': 5, 'Second': 6}
        self.template = '{}:' + ':'.join(['{:02}'] * 5)

    def _format(self, year, month=1, day=1, hour=0, minute=0, second=0):
        return self.template.format(year, month, day, hour, minute, second)

    def put(self, id, timestamp):
        """
        :type id: int
        :type timestamp: str
        :rtype: void
        """
        bisect.insort(self.seq, (timestamp, id))

    def retrieve(self, s, e, gra):
        """
        :type s: str
        :type e: str
        :type gra: str
        :rtype: List[int]
        """
        s = self._format(*[int(v) for v in s.split(':')[:self.gra[gra]]])
        e = [int(v) for v in e.split(':')[:self.gra[gra]]]
        e[-1] += 1
        e = self._format(*e)
        left = bisect.bisect_left(self.seq, (s, 0))
        right = bisect.bisect_right(self.seq, (e, 0))
        return [self.seq[i][1] for i in range(left, right)]





# Your LogSystem object will be instantiated and called as such:
obj = LogSystem()
obj.put(1, "2017:01:01:23:59:59")
obj.put(2, "2017:01:01:22:59:59")
obj.put(3, "2016:01:01:00:00:00")
print(obj.retrieve("2016:01:01:01:01:01","2017:01:01:23:00:00","Year"))
print(obj.retrieve("2016:01:01:01:01:01","2017:01:01:23:00:00","Hour"))
