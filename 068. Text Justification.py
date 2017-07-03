'''
Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly L characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

For example,
words: ["This", "is", "an", "example", "of", "text", "justification."]
L: 16.

Return the formatted lines as:

[
   "This    is    an",
   "example  of text",
   "justification.  "
]

Note: Each word is guaranteed not to exceed L in length.
'''


class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        def make_one_line(words):
            nSpace = len(words) - 1
            tSpace = maxWidth - sum(len(word) for word in words)
            theMin = tSpace // max(1, nSpace)
            nMax = tSpace - theMin * nSpace
            result = words[0]
            if nSpace == 0:
                result += ' ' * theMin
            for i in range(nSpace):
                result += (' ' * (theMin + 1 if i < nMax else theMin) +
                           words[i + 1])
            return result

        result = []
        i0 = tempSum = 0
        for i, word in enumerate(words):
            tempLen = len(word)
            if tempSum + tempLen > maxWidth:
                result.append(make_one_line(words[i0:i]))
                tempSum, i0 = 0, i
            tempSum += tempLen + 1
        tail = ' '.join(words[i0:])
        result.append(tail + ' ' * (maxWidth - len(tail)))
        return result


if __name__ == '__main__':
    Solution().fullJustify(
        ["Thisasdfas", "isasdfasdf", "an", "example", "of", "text", "justification."], 16)
