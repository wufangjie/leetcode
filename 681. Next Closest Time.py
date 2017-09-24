class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        limit = [int(time[0]) * 600, int(time[:2]) * 60]
        limit.append(limit[-1] + int(time[3]) * 10)
        limit.append(limit[-1] + int(time[4]))

        t0 = 60 * int(time[:2]) + int(time[3:])
        digits = set(map(int, time[:2] + time[3:]))
        theMin = float('inf')
        ret = '{0}{0}:{0}{0}'.format(min(digits))

        for d1 in digits:
            num = d1 * 600
            if d1 > 2 or num < limit[0]:
                continue
            for d2 in digits:
                num2 = num + d2 * 60
                if (d1 == 2 and d2 > 3) or num2 < limit[1]:
                    continue
                for d3 in digits:
                    num3 = num2 + d3 * 10
                    if d3 > 5 or num3 < limit[2]:
                        continue
                    for d4 in digits:
                        num4 = num3 + d4
                        if num4 > t0 and num4 < theMin:
                            theMin = num4
                            ret = '{}{}:{}{}'.format(d1, d2, d3, d4)
        return ret



print(Solution().nextClosestTime("19:34"), "19:39")
print(Solution().nextClosestTime("23:59"), "22:22")
