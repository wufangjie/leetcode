from functools import reduce


class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # return sorted(range(1, n + 1), key=str)

        # theLast = 10 ** (len(str(n)) - 1) - 1
        # if n >= theLast * 10:
        #     theLast = n

        count = 0
        result = [0] * n
        pre, pre_list = 1, [1]

        while count < n - 1:
            result[count] = pre
            if 10 * pre <= n:
                pre *= 10
                pre_list.append(0)
            elif pre_list[-1] != 9 and pre + 1 <= n:
                pre += 1
                pre_list[-1] += 1
            else:
                for i in range(len(pre_list) - 2, -1, -1):
                    if pre_list[i] != 9:
                        pre_list[i] += 1
                        pre = reduce(lambda x, y: 10 * x + y, pre_list[:i+1])
                        if pre <= n:
                            pre_list = pre_list[:i+1]
                            break
            count += 1

        result[-1] = pre
        return result



print(Solution().lexicalOrder(1130))
