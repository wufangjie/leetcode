from collections import Counter


class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        ns, np = len(s), len(p)
        if ns < np:
            return []

        count = Counter(p)
        current = {k: 0 for k in count}
        for i in range(np):
            if s[i] in count:
                current[s[i]] += 1
        diff = sum((abs(count[k] - current[k]) for k in count))
        result = [0] if diff == 0 else []
        for i in range(np, ns):
            if s[i] in count:
                diff += (1, -1)[count[s[i]] > current[s[i]]]
                current[s[i]] += 1
            if s[i - np] in count:
                diff += (1, -1)[count[s[i - np]] < current[s[i - np]]]
                current[s[i - np]] -= 1
            if diff == 0:
                result.append(i - np + 1)
            # print(diff) # influence speed a lot
        return result


print(Solution().findAnagrams("cbaebabacd", "abc"))
