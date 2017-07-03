from collections import Counter, deque, defaultdict


class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        n1 = len(s1)
        target = Counter(s1)
        current = defaultdict(deque)
        count = 0
        for i, c in enumerate(s2):
            if c in target:
                current[c].append(i)
                if len(current[c]) > target[c]:
                    count = 0
                    theMin = current[c][0]
                    for k, v in current.items():
                        while v and v[0] <= theMin:
                            v.popleft()
                        count += len(v)
                else:
                    count += 1
                    if count == n1:
                        return True

            else:
                current = defaultdict(deque)
                count = 0
        return False


assert Solution().checkInclusion("ab", "eidbaooo")
assert not Solution().checkInclusion("ab", "eidboaoo")
