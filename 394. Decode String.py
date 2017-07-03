class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        times, content, result = [], [], []
        num = 0
        for c in s:
            if c == '[':
                times.append(num)
                content.append([])
                num = 0
            elif c == ']':
                temp = times.pop() * ''.join(content.pop())
                if content:
                    content[-1].append(temp)
                else:
                    result.append(temp)
            elif '0' <= c <= '9':
                num = 10 * num + int(c)
            elif content:
                content[-1].append(c)
            else:
                result.append(c)
        return ''.join(result)

        # 35ms 91.78% vs 49ms 25.50%

        # times, content = [], []
        # num = 0
        # result = ''
        # for c in s:
        #     if c == '[':
        #         times.append(num)
        #         content.append('')
        #         num = 0
        #     elif c == ']':
        #         temp = times.pop() * content.pop()
        #         if content:
        #             content[-1] += temp
        #         else:
        #             result += temp
        #     elif '0' <= c <= '9':
        #         num = 10 * num + int(c)
        #     elif content:
        #         content[-1] += c
        #     else:
        #         result += c
        # return result


assert Solution().decodeString("3[a]2[bc]") == "aaabcbc"
assert Solution().decodeString("3[a2[c]]") == "accaccacc"
assert Solution().decodeString("2[abc]3[cd]ef") == "abcabccdcdcdef"
