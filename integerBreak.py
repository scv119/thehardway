import math
# leetcode: https://leetcode.com/problems/integer-break/description/

# dp solution
def integerBreak(self, n):
    # time complexity: O(n ^ 2), space complexity: O(n)
    result_list = [-1 for i in xrange(n+1)]
    result_list[0] = 0
    for i in xrange(1, n + 1, 1):
        max_result = 0
        for j in xrange(1, i):
            max_result = max(j * (i -j), result_list[j] * (i-j), result_list[i-j] * j, result_list[i - j] * result_list[j], max_result)
        result_list[i] = max_result
    return result_list[n]

# math solution
def integerBreak(self, n):
    # time complexity is O(lgn) as math.pow's time complexity is O(lgn)
    # space complexity: O(1)
    if n == 2:
        return 1
    elif n == 3:
        return 2
    elif n % 3 == 0:
        return int(math.pow(3, n / 3))
    elif n % 3 == 1:
        return 2 * 2 * int(math.pow(3, (n-4)/3))
    else:
        return 2 * int(math.pow(3, (n-2)/3))

