# leetcode: https://leetcode.com/problems/triangle/description/

def minimumTotal(self, triangle):
    # time O(n), space O(n), n is the number of all elements in triangle
    layer = len(triangle)
    result = [[-1 for i in xrange(j)] for j in xrange(1, layer+1)]
    result[0][0] = triangle[0][0]
    for i in xrange(1, layer):
        for j in xrange(0, i+1):
            if j == 0:
                result[i][j] = result[i-1][0] + triangle[i][j]
            elif j == i:
                result[i][j] = result[i-1][i-1] + triangle[i][j]
            else:
                result[i][j] = min(result[i-1][j-1], result[i-1][j]) + triangle[i][j]
    min_path = float("inf")
    for i in xrange(0, layer):
        min_path = min(min_path, result[layer-1][i])
    return min_path

def minimumTotal(self, triangle):
    # time: O(n^2), space O(n), n is the height of triangle
    layer = len(triangle)
    result = [0 for k in xrange(layer)]
    next_result = [0 for k in xrange(layer)]
    for i in xrange(1, layer):
        for j in xrange(0, i+1):
            if j == 0:
                next_result[j] = result[0] + triangle[i][j]
            elif j == i:
                next_result[j] = result[i-1] + triangle[i][j]
            else:
                next_result[j] = min(result[j-1], result[j]) + triangle[i][j]
        result = next_result[:]
    min_path = float("inf")
    for i in xrange(0, layer):
        min_path = min(min_path, result[layer-1][i])
    return min_path
