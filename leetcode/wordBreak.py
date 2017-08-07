# leetcode: https://leetcode.com/problems/word-break/#/description
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        : type s: str
        : type wordDict: List[str]
        : rtype: bool
        """
        for word in wordDict:
            if word == s:
                return True
            elif word in s:

