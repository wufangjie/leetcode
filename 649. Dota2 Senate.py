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
# explain
# Assume this round have been played smartly, except last RD, R have two choices ban the last D or ban the very first D still have right
# 1. If we want to proof case 2 is better, i.e. the last D will ban the very first R.
# 2. If first R is before first D, obviously it's a bad choice for R, so first R must be after first D, they will be banned together, this is no influence on the later play, the difference between case 1 and 2 is the first D have right or not.
# 3. Think about next round, if the R is banned, then the Ds will one more people to ban Rs, it's obviously worse, so if case 2 is better, we have the R will not be banned, this also mean Rs could have one more people to ban (since the last D has been banned in case 1, the people could be the very first D or later, then it's a draw)
# 4. so we have case 1 is always better
print(Solution().predictPartyVictory('RDDDRDRDRRDRRRDRRDRRDDDRDRRRDRRDRRRDRRDDDRDDRRRRDRDRDRDDDRDDRRRDDRRRDDDRDDDDDDRRRRDRRRRRRRRDDRDRDDDRRDDRRRDDRDDRRRRRDDDDRRDRDRRDRRRDDRDDRRRRDDDRRDRDRRDDDDDDDRDRRRDRRDRRDDDRDRRRDRRRDDDDRRRRDRRDRDDDDDDDRRDDRRDRDDRDRDRDRRDRRDRDRDRDDDRDRDDDDDDRRRRDDDDDRDDDDDDDRDDRDDRRRRDRRDRRDRDDRDRDDRDRRRRRDDRDRDDRRRRRDDDDDDDRDDRRDDRDRDRRDRDDRDRRDRRRRDDDRDDDDRRRDRDRRDDRDRDRRRDRDRDRRRRRDRRDDRRRDDDRRDRRRRDDRDRRRDRDRRRDRRDRRRRRRDRDRRDDRDRRDDDRRRRRRDDDDDDDDDDRRDRRDDRRRRDRRDRDDDDRRDDRDDDRDRRDRDRDRDRRDRDRDDRDDDRDRRDDRRRDDRDRDRDDDDRDRRRRDDRRRDRRRRDDDDDRRDDDDRDRRDDRDDRRRDDRDRDDRDDRDRRDRDDDRRDDRRRDDDDRRRRDDDRDDRRRRDDDDRRDRDDRRDDDRRDRRRRRDRRDDRRDDDDRDRRRDRRRDRRDRRDRDRRDDRRRRDRRDDDRRRDRDDDRRDDDDRRRRRDRDDDDRDRDRDRRRDDDDDDRDRDRRRDRRDRRRRDRRDRDRDDRRRDDDDRDRRDDDRDRDDDDDRRDDRRDRDRRRRDRRDDRRRDRDRDRDRRDDRDDRRRDDRDRRRRRRDRDRDDDRRDRRDDDDDDRRDRDDDDDRRDDDRRRRDRDRRRDDRDRRDRRRDDRDDRRRRDDDRRDDRDRRDRDRDRRDRDDRRDDRDDDRDDRDRDDDRDDDDDDDDRDDRRDRRRRDDRDDRDDDDDDDDDRRDRRDRRDDDRDRDDDRRRRDDDRRDRDDRRDDRRRDRRDRDDDDRRRDRDDDDRDDDRRRDDDRDDDRDRR'))
