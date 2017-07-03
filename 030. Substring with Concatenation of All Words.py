# NOTE: substring means continous

from collections import Counter, defaultdict, deque


class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        dct = Counter(words)
        ls = len(s)
        n, w = len(words), len(words[0])
        result = []
        for i in range(w):
            current = defaultdict(deque)
            count = 0
            for j in range(i, ls, w):
                word = s[j:j+w]
                if word not in dct:
                    current = defaultdict(deque)
                    count = 0
                else:
                    current[word].append(j)
                    count += 1
                    if len(current[word]) > dct[word]:
                        pos = current[word][0]
                        for k, v in current.items():
                            while v and v[0] <= pos:
                                v.popleft()
                                count -= 1

                    if count == n:
                        result.append(j - (n - 1) * w)
        return result


print(Solution().findSubstring("barfoothefoobarman", ["foo", "bar"]))

# 曾经一点思路也没有的题, 做到 600+ 之后, 再回头发现也不过如此
