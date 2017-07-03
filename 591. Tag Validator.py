import re


reg_wrapped = re.compile(r'^<([A-Z]{1,9})>(.*)</\1>$')
reg_cdata = re.compile(r'<!\[CDATA\[.*?\]\]>')
reg_tag = re.compile(r'<(/?[^<>]*)')
reg_valid_tag = re.compile(r'^/?[A-Z]{1,9}$')


class Solution(object):
    def isValid(self, code):
        """
        :type code: str
        :rtype: bool
        """
        temp = reg_wrapped.findall(code)
        if not temp:
            return False

        code = reg_cdata.sub('', temp[0][1])
        stack = []
        for match in reg_tag.finditer(code):
            tag = match.groups()[0]
            if not reg_valid_tag.match(tag):
                return False
            if tag[0] == '/':
                if not stack or stack[-1] != tag[1:]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(tag)
        return False if stack else True



assert Solution().isValid("<DIV>This is the first line <![CDATA[<div>]]></DIV>")
assert Solution().isValid("<DIV>>>  ![cdata[]] <![CDATA[<div>]>]]>]]>>]</DIV>")
assert not Solution().isValid("<A>  <B> </A>   </B>")
assert not Solution().isValid("<DIV>  div tag is not closed  <DIV>")
assert not Solution().isValid("<DIV>  unmatched <  </DIV>")
assert not Solution().isValid("<DIV> closed tags with invalid tag name  <b>123</b> </DIV>")
assert not Solution().isValid("<DIV> unmatched tags with invalid tag name  </1234567890> and <CDATA[[]]>  </DIV>")
assert not Solution().isValid("<DIV>  unmatched start tag <B>  and unmatched end tag </C>  </DIV>")

assert Solution().isValid("<A><A>/A></A></A>")
