from collections import deque


class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        n = len(senate)
        count_R = senate.count('R')
        if count_R < n * 0.3818:
            return 'Dire'
        elif count_R > n * 0.6182:
            return 'Radiant'

        R, D = [], []
        for i, c in enumerate(senate):
            if c == 'R':
                R.append(i)
            else:
                D.append(i)


        def rec(R, D):
            lr, ld = len(R), len(D)
            if lr < (lr + ld) * 0.3818:
                return 'Dire'
            if ld < (lr + ld) * 0.3818:
                return 'Radiant'

            R, D = deque(R), deque(D)
            R2, D2 = [], []
            while R and D:
                r, d = R.popleft(), D.popleft()
                if r < d:
                    R2.append(r)
                else:
                    D2.append(d)
            if R:
                R2.extend(R)
                D2 = D2[len(R):]
            elif D:
                D2.extend(D)
                R2 = R2[len(D):]
            return rec(R2, D2)

        return rec(R, D)


# about 1 - 0.3818, I guess the limit is golden section
# always ban the next coming thing, I can not promise is true, need time to think deeply
print(Solution().predictPartyVictory('RDDDRDRDRRDRRRDRRDRRDDDRDRRRDRRDRRRDRRDDDRDDRRRRDRDRDRDDDRDDRRRDDRRRDDDRDDDDDDRRRRDRRRRRRRRDDRDRDDDRRDDRRRDDRDDRRRRRDDDDRRDRDRRDRRRDDRDDRRRRDDDRRDRDRRDDDDDDDRDRRRDRRDRRDDDRDRRRDRRRDDDDRRRRDRRDRDDDDDDDRRDDRRDRDDRDRDRDRRDRRDRDRDRDDDRDRDDDDDDRRRRDDDDDRDDDDDDDRDDRDDRRRRDRRDRRDRDDRDRDDRDRRRRRDDRDRDDRRRRRDDDDDDDRDDRRDDRDRDRRDRDDRDRRDRRRRDDDRDDDDRRRDRDRRDDRDRDRRRDRDRDRRRRRDRRDDRRRDDDRRDRRRRDDRDRRRDRDRRRDRRDRRRRRRDRDRRDDRDRRDDDRRRRRRDDDDDDDDDDRRDRRDDRRRRDRRDRDDDDRRDDRDDDRDRRDRDRDRDRRDRDRDDRDDDRDRRDDRRRDDRDRDRDDDDRDRRRRDDRRRDRRRRDDDDDRRDDDDRDRRDDRDDRRRDDRDRDDRDDRDRRDRDDDRRDDRRRDDDDRRRRDDDRDDRRRRDDDDRRDRDDRRDDDRRDRRRRRDRRDDRRDDDDRDRRRDRRRDRRDRRDRDRRDDRRRRDRRDDDRRRDRDDDRRDDDDRRRRRDRDDDDRDRDRDRRRDDDDDDRDRDRRRDRRDRRRRDRRDRDRDDRRRDDDDRDRRDDDRDRDDDDDRRDDRRDRDRRRRDRRDDRRRDRDRDRDRRDDRDDRRRDDRDRRRRRRDRDRDDDRRDRRDDDDDDRRDRDDDDDRRDDDRRRRDRDRRRDDRDRRDRRRDDRDDRRRRDDDRRDDRDRRDRDRDRRDRDDRRDDRDDDRDDRDRDDDRDDDDDDDDRDDRRDRRRRDDRDDRDDDDDDDDDRRDRRDRRDDDRDRDDDRRRRDDDRRDRDDRRDDRRRDRRDRDDDDRRRDRDDDDRDDDRRRDDDRDDDRDRR'))
