class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        result, trace = [0] * n, []
        for row in logs:
            func_id, end, time = row.split(':')
            func_id, time = int(func_id), int(time)
            if end == 'end':
                _, pre = trace.pop()
                time += 1 - pre
                result[func_id] += time
                if trace:
                    result[trace[-1][0]] -= time
            else:
                trace.append((func_id, time))
        return result


print(Solution().exclusiveTime(3, ["0:start:0","1:start:2","1:start:3","2:start:4","2:end:5","1:end:6","1:end:7","0:end:8"]))
