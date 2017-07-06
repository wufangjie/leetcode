from collections import defaultdict


class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # the time limit is too tight
        # my solution is more clear and when A has many duplicate number will faster
        # slices, pairs, count = defaultdict(int), defaultdict(int), defaultdict(int)
        # for elem in A:
        #     for pre in count:
        #         d = elem - pre
        #         slices[d, elem] += slices[d, pre] + pairs[d, pre]
        #         pairs[d, elem] += count[pre]
        #     count[elem] += 1
        # return sum(slices.values())



        n = len(A)
        dp = [defaultdict(int) for i in range(n)]
        res = 0
        for i in range(1, n):
            for j in range(i):
                d = A[i] - A[j]
                dp[i][d] += dp[j][d] + 1
                res += dp[j][d]
        return res




# print(Solution().numberOfArithmeticSlices([2, 4, 6, 8, 10]))
# print(Solution().numberOfArithmeticSlices([2,2,3,4]))
print(Solution().numberOfArithmeticSlices([2,2,3,4,4,5,4,5,1,2,3,4,5,6]))

print(Solution().numberOfArithmeticSlices([1,2,3,1,2,3]))

import time
tic = time.time()
print(Solution().numberOfArithmeticSlices([2147483567,2147482946,2147483525,2147483135,2147482796,2147483313,2147482733,2147482874,2147483252,2147483266,2147482924,2147482949,2147483106,2147483409,2147482665,2147483272,2147483181,2147483593,2147483601,2147482945,2147483368,2147482675,2147483406,2147482692,2147483403,2147483196,2147482963,2147483274,2147483600,2147483346,2147483163,2147483354,2147483313,2147483442,2147482709,2147482729,2147483330,2147482906,2147483398,2147483045,2147483363,2147483517,2147483364,2147483318,2147482907,2147482898,2147482675,2147483477,2147483095,2147482994,2147483103,2147482813,2147483572,2147482670,2147482923,2147482715,2147482673,2147482663,2147482930,2147482736,2147482778,2147483310,2147483455,2147482870,2147482886,2147482816,2147482826,2147483487,2147483639,2147483576,2147483379,2147482971,2147483453,2147482969,2147483382,2147482958,2147482728,2147482780,2147482721,2147482667,2147483206,2147483175,2147482742,2147483279,2147482839,2147483444,2147483585,2147482914,2147483104,2147482934,2147483267,2147482672,2147482723,2147483389,2147482722,2147483221,2147483248,2147483612,2147483452,2147483592,2147483075,2147482869,2147483496,2147482922,2147483388,2147482827,2147482657,2147483294,2147482695,2147482903,2147482789,2147483175,2147482663,2147483165,2147483368,2147482915,2147483551,2147482652,2147482848,2147483447,2147482982,2147483164,2147482856,2147482690,2147483358,2147482930,2147482814,2147482668,2147482915,2147482724,2147483575,2147483197,2147483479,2147482850,2147483194,2147482887,2147482845,2147483077,2147483260,2147483410,2147482964,2147482709,2147483322,2147482775,2147482988,2147483554,2147482686,2147483600,2147483545,2147483042]))
print(Solution().numberOfArithmeticSlices([6173,5762,-5056,724,-5813,-907,3628,-1081,-2837,3882,6358,-10206,4842,-10079,11008,-1357,8098,8191,-10970,5570,-10212,-9125,-5386,-2774,-398,-1471,-6676,-9519,5369,3637,-2102,-8716,-8593,183,-5562,8803,-2059,10234,10720,-9146,7532,7109,8593,-8327,334,-3896,10628,8963,7401,-11119,10355,-9236,-221,2904,-10085,3339,10983,-9470,-10408,5589,-9082,8832,-9360,345,-3497,8035,4549,-4850,-1939,-7255,7374,-4541,2962,9354,6529,-7864,-3148,6247,-2823,9048,-6881,-4024,-1041,1234,-10294,-228,-6862,8680,11212,-6127,9118,3963,8135,-4477,2996,-6606,4663,4102,-9101,-9791,4941,6794,-5272,-10876,7712,-6770,-6515,1990,9304,-3456,-9492,-10693,-4237,-2870,-8795,-8807,-1365,7045,-4850,-9693,-6194,10242,-3372,-9120,-1693,-4835,4816,-11051,-2978,9947,-4014,8140,3271,9087,-3055,4823,3808,-3917,-11158,-6116,-275,-9678,9854,-1428,5931,626,4162,-1357,7017,-1051,10649,-7202,-3926,-6518,-9352,-5371,-3344,-2966,-2758,-7738,7469,-3262,9339,-8382,2601,10775,-8587,-8754,372,-9897,-3374,1072,-5791,-2557,9122,-1824,5180,4212,9572,-6702,11178,-1623,-1362,4104,7660,-9162,10094,6385,10366,8464,-5668,4266,7554,10230,9365,-559,9157,-1373,-6697,-2051]))
print(time.time() - tic)