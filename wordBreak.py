# leetcode: https://leetcode.com/problems/word-break/description/

def wordBreak(self, s, wordDict):
    # time complexity: O(n*n), space: O(n)
    dp = (len(s) + 1) * [False]
    dp[0] = True
    for i in xrange(1, len(s) + 1):
        for j in xrange(0, i):
            if dp[j] == True:
                if s[j:i] in wordDict:
                    dp[i] = True
                    break
    return dp[len(s)]
