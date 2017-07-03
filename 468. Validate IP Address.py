import re

# reg_ipv4 = re.compile('((25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\.){3}(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)$')
# reg_ipv6 = re.compile(r'(?:[0-9a-fA-F]{1,4}\:){7}[0-9a-fA-F]{1,4}$')
# NOTE: {1,4} no space

reg_ipv4 = re.compile('(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)$')
reg_ipv6 = re.compile(r'[0-9a-fA-F]{1,4}$')


class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        part = IP.split('.')
        if len(part) == 4:
            if all(map(reg_ipv4.match, part)):
                return 'IPv4'
        elif len(part) == 1:
            part = IP.split(':')
            if len(part) == 8 and all(map(reg_ipv6.match, part)):
                return 'IPv6'
        return 'Neither'


        # if reg_ipv6.match(IP):
        #     return 'IPv6'
        # elif reg_ipv4.match(IP):
        #     return 'IPv4'
        # else:
        #     return 'Neither'


# print(reg_ipv6.match('2001:0db8:85a3:0000:0000:8a2e:0370:7334')) # valid
# print(reg_ipv6.match('2001:db8:85a3:0:0:8A2E:0370:7334')) # valid
# print(reg_ipv6.match('2001:0db8:85a3::8A2E:0370:7334')) # invalid
# print(reg_ipv6.match('02001:0db8:85a3:0000:0000:8a2e:0370:7334')) # invalid

print(Solution().validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334:"))
print(reg_ipv4.match("2001:0db8:85a3:0:0:8A2E:0370:7334:"))
