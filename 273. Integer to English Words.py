class Solution(object):
    basic = {'0': '',
             '1': 'One',
             '2': 'Two',
             '3': 'Three',
             '4': 'Four',
             '5': 'Five',
             '6': 'Six',
             '7': 'Seven',
             '8': 'Eight',
             '9': 'Nine'}

    teen = {'10': 'Ten',
            '11': 'Eleven',
            '12': 'Twelve',
            '13': 'Thirteen',
            '14': 'Fourteen',
            '15': 'Fifteen',
            '16': 'Sixteen',
            '17': 'Seventeen',
            '18': 'Eighteen',
            '19': 'Nineteen'}

    ty = {'2': 'Twenty',
          '3': 'Thirty',
          '4': 'Forty',
          '5': 'Fifty',
          '6': 'Sixty',
          '7': 'Seventy',
          '8': 'Eighty',
          '9': 'Ninety'}

    comma = {-12: 'Billion', -9: 'Million', -6: 'Thousand'}


    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return 'Zero'
        num_str = str(num)
        n = len(num_str)
        start = -((n + 2) // 3 * 3)
        result = []
        for i in range(start, -3, 3):
            test = self.convert3(num_str[i:i+3])
            if test:
                result.append(test)
                result.append(self.comma[i])
        test = self.convert3(num_str[-3:])
        if test:
            result.append(test)
        return ' '.join(result)

    def convert3(self, num_str):
        result = []
        n = len(num_str)
        if n == 3:
            if self.basic[num_str[0]]:
                result.append(self.basic[num_str[0]])
                result.append('Hundred')
        if n >= 2:
            if num_str[-2:] in self.teen:
                result.append(self.teen[num_str[-2:]])
                return ' '.join(result)
            elif num_str[-2] != '0':
                result.append(self.ty[num_str[-2]])

        if self.basic[num_str[-1]]:
            result.append(self.basic[num_str[-1]])
        return ' '.join(result)


if __name__ == '__main__':
    assert Solution().numberToWords(123) == "One Hundred Twenty Three"
    assert Solution().numberToWords(12345) == "Twelve Thousand Three Hundred Forty Five"
    assert Solution().numberToWords(1234567) == "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
