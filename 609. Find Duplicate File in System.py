import re
from collections import defaultdict


reg_file_and_content = re.compile(r'(.+?)\((.+?)\)')


class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        dct = defaultdict(list)
        for p in paths:
            # d, *fs = p.split(' ') # python2 not support this
            parts = p.split(' ')
            d = parts[0]
            for f in parts[1:]:
                temp = reg_file_and_content.findall(f)[0]
                dct[temp[1]].append('{}/{}'.format(d, temp[0]))
        return [v for v in dct.values() if len(v) > 1]

# NOTE: only return duplicate



print(Solution().findDuplicate(["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]))
