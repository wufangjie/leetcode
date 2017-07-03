class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return word.isupper() or word.islower() or word.istitle()
        # if (word == word.upper() or word == word.lower()
        #     or word == word.capitalize()):
        #     return True
        # else:
        #     return False
