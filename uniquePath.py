# leetcode: https://leetcode.com/problems/unique-paths/description/

def uniquePath(self, m, n):
    # in python 2-d array cannot be initialized as [[1]*n] * m !!!!!
    # time: O(n*m), space O(n*m)
    dp = [[1] * n for i in xrange(m)]
    dp[0][0] = 1
    for i in xrange(1, m):
        for j in xrange(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[m-1][n-1]
