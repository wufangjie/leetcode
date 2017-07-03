class Codec:
    def __init__(self):
        self.chs = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.count = 0
        self.lst = []
        self.dct = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        if longUrl in self.dct:
            return self.dct[longUrl]
        else:
            short = self.n2s(self.count)
            self.lst.append(longUrl)
            self.count += 1
            self.dct[longUrl] = short
            return short

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        return self.lst[self.s2n(shortUrl)]

    def n2s(self, num):
        result = ['0'] * 6
        for i in range(5, -1, -1):
            result[i] = self.chs[num % 62]
            num //= 62
        return ''.join(result)

    def s2n(self, string):
        n = 0
        for c in string:
            d = ord(c)
            n *= 10
            if d <= 57:
                n += d - 48
            elif d <= 90:
                n += d - 55 # 65 + 10
            else:
                n += d - 61 # 97 + 10 + 26
        return n





# Your Codec object will be instantiated and called as such:
codec = Codec()
print(codec.decode(codec.encode('asdfasdfsf')))
print(codec.decode(codec.encode('asdfsfsffs')))
