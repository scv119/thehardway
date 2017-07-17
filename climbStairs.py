class Solution(object):
    def climbStairs(self, n):
        """
        : type n: int
        : rtype: int
        """
        #second solution
        # to make solution time complexity O(n)
        # f(n) = f(n -1) + f(n-2)
        # use a list to memorize previous solution
        result = []
        result.append(1)
        result.append(1)
        for i in range(2, n+1):
            result.append(result[i-2]+result[i-1])
        return result[n]

    def climbStairs2(self, n):
        #initial solution
        # n = 1, one solution
        # n >= 2, two categories: 1, last step: 2  or 2, last step: 1
        # f(n) = f(n-1) + f(n-2) fibonacci
        if n == 0:
            return 1
        elif n == 1:
            return 1
        elif n > 1:
            return self.climbStairs2(n-1) + self.climbStairs2(n-2)

a = Solution()
print "solution1"
for i in range(0, 60):
    print a.climbStairs(i)
print "solution2"
for i in range(0, 60):
    print a.climbStairs2(i)
