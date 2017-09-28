class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        # python2's True and False is slow
        limit = tuple(map(int, time[:2] + time[3:]))
        digits = sorted(set(limit))

        for d1 in digits:
            if d1 > 2:
                break
            if d1 < limit[0]:
                continue
            equal = 1 if d1 == limit[0] else 0
            for d2 in digits:
                if (d1 == 2 and d2 > 3):
                    break
                if equal:
                    if d2 < limit[1]:
                        continue
                    elif d2 > limit[1]:
                        equal = 0
                for d3 in digits:
                    if d3 > 5:
                        break
                    if equal:
                        if d3 < limit[2]:
                            continue
                        elif d3 > limit[2]:
                            equal = 0
                    for d4 in digits:
                        if not equal or d4 > limit[3]:
                            return '{}{}:{}{}'.format(d1, d2, d3, d4)
        return '{0}{0}:{0}{0}'.format(digits[0])




print(Solution().nextClosestTime("19:34"), "19:39")
print(Solution().nextClosestTime("23:59"), "22:22")
