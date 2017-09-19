# leetcode: https://leetcode.com/problems/perfect-squares/description/

def numSquares(self, n):
    # time: O(n*sqrt(n)), space O(n)
    dp = [0, 1]
    for i in xrange(2, n+1):
        temp = float("inf")
        j = 1
        while j * j <= i:
            temp = min(temp, 1 + dp[i - j * j])
            j = j + 1
        dp.append(temp)
    return dp[n]
