from collections import Counter


seq = [(23, 6, [18]),
       (22, 2, [14]),
       (20, 4, [14, 5]),
       (25, 0, [14]),
       ( 6, 8, [7]),
       ( 5, 5, []),
       (18, 7, [13]),
       ( 7, 3, []),
       (14, 1, [13])]


class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = [0] * 26
        for k, v in Counter(s).items():
            count[ord(k) - 97] += v
        result = [0] * 10
        for i, n, to_minus in seq:
            if count[i] > 0:
                result[n] = count[i]
                for j in to_minus:
                    count[j] -= count[i]
        result[9] = count[13] // 2
        return ''.join([str(i) * v for i, v in enumerate(result)])



# seq = [(23, '6', [18]),
#        (22, '2', [14]),
#        (20, '4', [14, 5]),
#        (25, '0', [14]),
#        ( 6, '8', [7]),
#        ( 5, '5', []),
#        (18, '7', [13]),
#        ( 7, '3', []),
#        (14, '1', [13])]

        # count = [0] * 26
        # for k, v in Counter(s).items():
        #     count[ord(k) - 97] += v
        # result = []
        # for i, n, to_minus in seq:
        #     if count[i] > 0:
        #         result.append(n * count[i])
        #         for j in to_minus:
        #             count[j] -= count[i]
        # result.append('9' * (count[13] // 2))
        # return ''.join(sorted(result)) # sort is costly? perhaps not


# NOTE: 终于看明白了是单个数字, 不是组合在一起





# from collections import Counter
# print(Counter('zeroonetwothreefourfivesixseveneightnine'))
# print(Counter('onethreefivesevennine'))

# seq = [('x', '6', 'six'),
#        ('w', '2', 'two'),
#        ('u', '4', 'four'),
#        ('z', '0', 'zero'),
#        ('g', '8', 'eight'),
#        ('f', '5', 'five'),
#        ('s', '7', 'seven'),
#        ('h', '3', 'three'),
#        ('o', '1', 'one')]

# seq = [(ord(c) - 97, n, [(ord(k) - 97, v) for k, v in Counter(word).items()])
#         for c, n, word in seq]


# seq = [(23, '6', [(18, 1), (8, 1)]),
#        (22, '2', [(22, 1), (14, 1), (19, 1)]),
#        (20, '4', [(14, 1), (17, 1), (5, 1), (20, 1)]),
#        (25, '0', [(25, 1), (17, 1), (14, 1), (4, 1)]),
#        ( 6, '8', [(6, 1), (4, 1), (19, 1), (8, 1), (7, 1)]),
#        ( 5, '5', [(4, 1), (5, 1), (21, 1), (8, 1)]),
#        (18, '7', [(18, 1), (4, 2), (13, 1), (21, 1)]),
#        ( 7, '3', [(17, 1), (4, 2), (7, 1), (19, 1)]),
#        (14, '1', [(13, 1), (4, 1), (14, 1)])]



# seq = [('x', '6', 's'),
#        ('w', '2', 'o'),
#        ('u', '4', 'fo'),
#        ('z', '0', 'o'),
#        ('g', '8', 'h'),
#        ('f', '5', ''),
#        ('s', '7', 'n'),
#        ('h', '3', ''),
#        ('o', '1', 'n')]


# seq = [(ord(c) - 97, n, [(ord(k) - 97, v) for k, v in Counter(word).items()])
#         for c, n, word in seq]
# pprint(seq)


assert Solution().originalDigits("owoztneoer") == "012"
assert Solution().originalDigits("fviefuro") == "45"
