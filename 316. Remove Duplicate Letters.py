# good question


class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)

        last_index = {}
        for i, elem in enumerate(s):
            last_index[elem] = i

        seq = sorted(((idx, k) for k, idx in last_index.items()))
        select = {}
        start = 0
        for idx, k in seq:
            if k not in select:
                for p, i in sorted([(s[i], i) for i in range(start, idx + 1)
                                    if s[i] <= k and s[i] not in select]):
                    if p not in select and i >= start:
                        select[p] = i
                        start = i + 1
        return ''.join(sorted(select.keys(), key=lambda x: select[x]))


        ############################################################
        # try2 **only no smaller element before is also not enough**
        ############################################################
        # n = len(s)

        # last_index = {}
        # for i, elem in enumerate(s):
        #     last_index[elem] = i

        # seq = sorted(((idx, k) for k, idx in last_index.items()))
        # select = {}
        # start = 0
        # for idx, k in seq:
        #     if k not in select:
        #         before = sorted([(s[i], i) for i in range(start, idx)
        #                          if s[i] < k and s[i] not in select])
        #         if before:
        #             select[k] = idx
        #             i_left = start
        #             for p, i in before:
        #                 if p not in select and i >= i_left:
        #                     select[p] = i_left = i
        #             start = idx + 1
        #         else:
        #             while s[start] != k:
        #                 start += 1
        #             select[k] = start
        #             start += 1
        # return ''.join(sorted(select.keys(), key=lambda x: select[x]))


        ############################################################
        # try1 **only minimun among left (leave) is not enough**
        ############################################################
        # n = len(s)

        # last_index = {}
        # for i, elem in enumerate(s):
        #     last_index[elem] = i

        # seq = sorted(((idx, k) for k, idx in last_index.items()))
        # left = sorted(last_index.keys(), reverse=True)
        # select = {}
        # start = 0
        # for idx, k in seq:
        #     if k not in select:
        #         while left[-1] in select:
        #             left.pop()
        #         if k == left[-1]: # if k is minimun among left, choose the first
        #             while s[start] != k:
        #                 start += 1
        #             select[k] = start
        #             start += 1
        #         else:
        #             select[k] = idx
        #             i_left = start
        #             for p, i in sorted([(s[i], i) for i in range(start, idx)
        #                                 if s[i] < k and s[i] not in select]):
        #                 if p not in select and i >= i_left:
        #                     select[p] = i_left = i
        #             start = idx + 1
        # return ''.join(sorted(select.keys(), key=lambda x: select[x]))



assert Solution().removeDuplicateLetters("bcabc") == "abc"
assert Solution().removeDuplicateLetters("cbacdcbc") == "acdb"
assert Solution().removeDuplicateLetters("bbcaac") == 'bac'
assert Solution().removeDuplicateLetters("abacb") == 'abc'
assert Solution().removeDuplicateLetters("mitnlruhznjfyzmtmfnstsxwktxlboxutbic") == "ilrhjfyzmnstwkboxuc"
assert Solution().removeDuplicateLetters("wmxkuuoordmnpnebikzzujdpscpedcrsjphcaykjsmobturjjxxpoxvvrynmapegvtlasmyuddgxygkaztmbpkrnukbxityz") == "wbcdhajmoegvlskprnuxityz"
