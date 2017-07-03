from itertools import combinations, product


class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        result = []
        for i in range(5):
            j = num - i
            if not 0 <= j <= 8:
                continue

            if i != 0:
                c1 = []
                for c in combinations((1, 2, 4, 8), i):
                    temp = sum(c)
                    if temp < 12:
                        c1.append(temp)
            else:
                c1 = [0]

            if j != 0:
                c2 = []
                for c in combinations((1, 2, 4, 8, 16, 32), j):
                    temp = sum(c)
                    if temp < 60:
                        c2.append(temp)
            else:
                c2 = [0]

            for h, m in product(c1, c2):
                result.append('{}:{:02d}'.format(h, m))
        return result


# # NOTE: 12:01 is not valid time for the watch
# # NOTE: 12:00 is also not valid
# assert sorted(Solution().readBinaryWatch(3)) == sorted(["0:07","0:11","0:13","0:14","0:19","0:21","0:22","0:25","0:26","0:28","0:35","0:37","0:38","0:41","0:42","0:44","0:49","0:50","0:52","0:56","1:03","1:05","1:06","1:09","1:10","1:12","1:17","1:18","1:20","1:24","1:33","1:34","1:36","1:40","1:48","2:03","2:05","2:06","2:09","2:10","2:12","2:17","2:18","2:20","2:24","2:33","2:34","2:36","2:40","2:48","3:01","3:02","3:04","3:08","3:16","3:32","4:03","4:05","4:06","4:09","4:10","4:12","4:17","4:18","4:20","4:24","4:33","4:34","4:36","4:40","4:48","5:01","5:02","5:04","5:08","5:16","5:32","6:01","6:02","6:04","6:08","6:16","6:32","7:00","8:03","8:05","8:06","8:09","8:10","8:12","8:17","8:18","8:20","8:24","8:33","8:34","8:36","8:40","8:48","9:01","9:02","9:04","9:08","9:16","9:32","10:01","10:02","10:04","10:08","10:16","10:32","11:00"])

print(sorted(Solution().readBinaryWatch(2)))
