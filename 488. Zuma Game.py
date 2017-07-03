from collections import defaultdict, Counter


class Solution(object):
    def findMinStep(self, board, hand):
        """
        :type board: str
        :type hand: str
        :rtype: int
        """
        count = Counter(hand)
        # position = defaultdict(list)

        # for i, b in enumerate(board):
        #     position[b].append(i)

        # for k, v in position.items():
        #     if len(v) + count.get(k, 0) < 3:
        #         return -1

        def rec(left, used, count, best):
            if not left:
                best[0] = min(used, best[0])
            if used >= best[0] or sum(count.values()) == 0:
                return

            used += 1
            for k, v in count.items():
                count2 = count.copy()
                if v == 1:
                    count2.pop(k)
                else:
                    count2[k] -= 1

                for i in range(len(left)):
                    if left[i] == k and (i == 0 or left[i - 1] != k): # i == 0
                        if i < len(left) - 1 and left[i + 1] == k:
                            left2 = self.combine(left[:i] + left[i+2:], i)
                        else:
                            left2 = left[:i] + k + left[i:]
                        rec(left2, used, count2, best)

        best = [float('inf')]
        rec(board, 0, count, best)
        return -1 if best[0] == float('inf') else best[0]

    @staticmethod
    def combine(left, i):
        while i > 0:
            ll = len(left)
            if i == ll:
                break
            elif i == ll - 1:
                k = ll
            else:
                for k in range(i + 1, ll):
                    if left[k] != left[i]:
                        break
                else:
                    k += 1
            for j in range(i - 1, -1, -1):
                if left[j] != left[i]:
                    break
            else:
                j -= 1

            if k - j > 3:
                left = left[:j+1] + left[k:]
                i = j + 1
            else:
                break
        return left



assert Solution().findMinStep('GYYGBYYBGG', 'YBYGG') == 3
assert Solution().findMinStep('GGYYGGYYGG', 'GGYY') == 1
assert Solution().findMinStep('GYGYGYG', 'GGGGGGYYYYYY') == 5
assert Solution().findMinStep("WWRRBBWW", "WRBRW") == 2
assert Solution().findMinStep("R", "RR") == 2
assert Solution().findMinStep("RRWWRRW", "WWRRR") == 2
