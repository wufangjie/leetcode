from collections import defaultdict
import bisect
from utils import memo


class Solution(object):
    def findRotateSteps(self, ring, key):
        """
        :type ring: str
        :type key: str
        :rtype: int
        """
        m, n = len(ring), len(key)
        mid = (m >> 1) + 1

        dct = defaultdict(list)
        for i, c in enumerate(ring):
            dct[c].append(i)
        only_once = {k for k, v in dct.items() if len(v) == 1}

        @memo
        def dfs(i, pre, key):
            if i == len(key):
                return 0

            arr = dct[key[i]]
            if len(arr) == 1:
                temp = abs(pre - arr[0])
                return min(temp, m - temp)

            j = bisect.bisect(arr, pre)
            stp, nxt = [], []
            if j == len(arr) or j == 0:
                if j == 0:
                    if arr[0] - pre < mid:
                        stp.append(arr[0] - pre)
                        nxt.append(arr[0])
                    if pre + m - arr[-1] < mid:
                        stp.append(pre + m - arr[-1])
                        nxt.append(arr[-1])
                else:
                    if pre - arr[-1] < mid:
                        stp.append(pre - arr[-1])
                        nxt.append(arr[-1])
                    if arr[0] + m - pre < mid:
                        stp.append(arr[0] + m - pre)
                        nxt.append(arr[0])
            else:
                if pre - arr[j - 1] < mid:
                    stp.append(pre - arr[j - 1])
                    nxt.append(arr[j - 1])
                if arr[j] - pre < mid:
                    stp.append(arr[j] - pre)
                    nxt.append(arr[j])
            return min(s + dfs(i + 1, t, key) for s, t in zip(stp, nxt))

        total = n
        pre = 0
        part = []
        for i in range(n):
            if i == 0 or key[i] != key[i - 1]:
                part.append(key[i])
                if key[i] in only_once:
                    total += dfs(0, pre, ''.join(part))
                    pre = dct[key[i]][0]
                    part = []
        if part:
            total += dfs(0, pre, ''.join(part))

        return total


# assert Solution().findRotateSteps("godding", "gd") == 4
# assert Solution().findRotateSteps("godding", "gdi") == 7
# assert Solution().findRotateSteps("edcba", "abcde") == 10
# assert Solution().findRotateSteps("ababcab", "acbaacba") == 17
print(Solution().findRotateSteps("fhkfmhkmdk", "fkdkkkdkmfmkkmdkfdmmmfmhffdkhfhhfhfmfhmfmhhmmkkmkhhkhkhkmfhmmmhhkmdkfkkkfdhkdfhdfkkdfkkkfkfhmhkkfmkh"))
