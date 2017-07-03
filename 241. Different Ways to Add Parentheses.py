from itertools import permutations


class Solution(object):
    op_dict = {'+': lambda x, y: x + y,
               '-': lambda x, y: x - y,
               '*': lambda x, y: x * y,
               '/': lambda x, y: x // y}

    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        nums, ops, temp = [], [], []
        for c in input:
            if c in self.op_dict:
                nums.append(int(''.join(temp)))
                ops.append(c)
                temp = []
            else:
                temp.append(c)
        nums.append(int(''.join(temp)))


        def cal(comb):
            nums2 = nums[:]
            for i in comb:
                op = ops[i]
                l = i
                while nums2[l] is None:
                    l -= 1
                r = i + 1
                while nums2[r] is None:
                    r += 1
                nums2[l] = self.op_dict[op](nums2[l], nums2[r])
                nums2[r] = None
            return nums2[l]


        n = len(ops)
        if n == 0:
            return nums
        results = []
        for comb in permutations(range(n)):
            test = [[comb[0], comb[0]]]
            cal_flag = True
            for i in range(1, n):
                if test[-1][0] - comb[i] > 1:
                    cal_flag = False
                    break
                elif test[-1][0] - comb[i] == 1:
                    if len(test) > 1 and test[-2][1] == comb[i] - 1:
                        _, temp = test.pop()
                        test[-1][1] = temp
                    else:
                        test[-1][0] = comb[i]
                elif comb[i] - test[-1][1] > 1:
                    test.append([comb[i], comb[i]])
                else:
                    test[-1][1] = comb[i]
            if cal_flag:
                results.append(cal(comb))
        return results


# Solution().diffWaysToCompute('2-1-1')
# Solution().diffWaysToCompute("2*3-4*5")
