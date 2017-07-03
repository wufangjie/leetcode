# can not change order

class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        maxlen = len(s)
        mini = ([(i - 1, i + 1) for i in range(1, maxlen - 1)
                 if s[i - 1] == s[i + 1]]
                + [(i - 1, i) for i in range(1, maxlen) if s[i - 1] == s[i]])

        def _expand(lo, hi):
            while lo >= 0 and hi < maxlen:
                if s[lo] != s[hi]:
                    return lo + 1, hi - 1
                lo -= 1
                hi += 1
            else:
                return lo + 1, hi - 1

        spans = sorted((_expand(i, j) for i, j in mini),
                       key=lambda x: x[0] + x[1]) # sorted by middle
        n = len(spans)

        # import pdb
        # pdb.set_trace()
        def combine(pre, i, results):
            if i == n:
                results.append(pre)
            else:
                a, b = spans[i]
                for j in range((b - a + 1) >> 1):
                    if not pre or pre[-1][1] < a + j:
                        combine(pre + [(a+j, b-j)], i+1, results)
                combine(pre, i+1, results)

        results = []
        combine([], 0, results)

        s_list = list(s)
        results_show = []
        for parts in results:
            if not parts:
                results_show.append(s_list)
            else:
                temp = s_list[: parts[0][0]]
                for i, (a, b) in enumerate(parts):
                    temp.append(''.join(s_list[a:b+1]))
                    try:
                        temp.extend(s_list[b+1 : parts[i+1][0]])
                    except IndexError:
                        temp.extend(s_list[b+1 :])
                results_show.append(temp)
        return results_show


if __name__ == '__main__':
    xx = sorted(Solution().partition("amanaplanacanalpanama"))
