# leetcode https://leetcode.com/problems/unique-binary-search-trees/tabs/description/

class Solution(object):
    def numTrees(self, n):
        """
        : type n: int
        : rtype: int
        """
        # rule: f(n) = f(0) * f(n-1) + f(1) * f(n-2) + ... + f(n-1) f(0), f(0) = 1
        # time complexity: O(n^2)
        result = [1]
        i = 1
        while i <= n:
            temp = 0
            for j in xrange(0, i):
                temp = temp + result[j] * result[i - 1 - j]
            result.append(temp)
            i = i + 1
        return result[n]
