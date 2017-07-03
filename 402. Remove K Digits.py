import heapq


class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        n = len(num)
        idx0 = [i for i, c in enumerate(num) if c == '0']
        len0 = len(idx0)

        if n - k <= len0:
            return '0'

        start = i = 0
        while i < len0:
            if k + i >= idx0[i]:
                i += 1
            else:
                if i != 0:
                    start = idx0[i - 1] + 1
                end = idx0[i]
                break
        else:
            end = n

        need_left = end - start - (k - start + i)
        H = [(num[i], i) for i in range(start, end)]
        heapq.heapify(H)
        result, reconsider = [], []
        while need_left:
            v, l = heapq.heappop(H)
            if l < start:
                continue
            elif end - l == need_left:
                return ''.join(result) + num[l:]
            elif end - l > need_left:
                result.append(v)
                start = l
                H = reconsider + H
                need_left -= 1
            else:
                reconsider.append((v, l))
        return ''.join(result) + num[end:]



assert Solution().removeKdigits('123', 3) == '0'
assert Solution().removeKdigits("1432219", 3) == '1219'
assert Solution().removeKdigits("10200", 1) == '200'
assert Solution().removeKdigits("2525497023016795374275732785188831947517151146214923806485309183076276545212503868281039301565753044", 20) == '122785188831947517151146214923806485309183076276545212503868281039301565753044'
assert Solution().removeKdigits("112", 1) == '11'
