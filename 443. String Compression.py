class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        n = len(chars)
        if n < 2:
            return n

        chars.append('')
        count = 0
        pre_i, pre_c = -1, ''
        for i, c in enumerate(chars):
            if c != pre_c:
                chars[count - 1] = pre_c
                if i > pre_i + 1:
                    temp = str(i - pre_i)
                    tempN = len(temp)
                    chars[count:count+tempN] = temp
                    count += tempN
                count += 1
                pre_i, pre_c = i, c
        return count - 1


chars = ["a","a","b","b","c","c","c"]
print(Solution().compress(chars))
print(chars)

chars = ["a", "a"]
print(Solution().compress(chars))
print(chars)


chars = ["a", "b"]
print(Solution().compress(chars))
print(chars)


chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
print(Solution().compress(chars))
print(chars)
