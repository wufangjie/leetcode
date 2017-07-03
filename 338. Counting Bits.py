class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        result = [0] * (num + 1)

        for i in range(1, num + 1):
            if i & 1:
                result[i] = result[i-1] + 1
            else:
                result[i] = result[i >> 1]
        return result

# 一开始没太明白题目, 返回 0 <= i <= num 的二进制表示的 1 个个数的列表
print(Solution().countBits(5))
print(Solution().countBits(20))
