'''
There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.

Note:
The solution is guaranteed to be unique.
'''

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        start, n = 0, len(cost)
        while start < n:
            gas_in_car = 0
            for i in range(start, start + n):
                i %= n
                gas_in_car += gas[i] - cost[i]
                if gas_in_car < 0:
                    break
            else:
                return start
            start = i + n + 1 if i < start else i + 1
        return -1 if n != 0 else 0


if __name__ == '__main__':
    Solution().canCompleteCircuit([2, 4], [3, 4])
