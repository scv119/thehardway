# leetcode: https://leetcode.com/problems/minimum-path-sum/description/

def minPathSum(self, grid):
    height = len(grid)
    width = len(grid[0])
    return self.minPathHelper(grid, height - 1, width - 1)

def minPathHelper(self, grid, i, j):
    if i == 0 and j == 0:
        return grid[i][j]
    elif i == 0:
        return self.minPathHelper(grid, i, j - 1) + grid[i][j]
    elif j == 0:
        return self.minPathHelper(grid, i - 1, j) + grid[i][j]
    elif i >= 1 and j >= 1:
        return min(self,minPathHelper(grid, i - 1, j), self.minPathHelper(grid, i, j - 1)) + grid[i][j]


def minPathSum(self, grid):
    # time: O(n*m), space O(n*m), n is the height of grid, and m is the width of grid
    height = len(grid)
    width = len(grid[0])
    reuslt = [[0 for i in xrange(width)] for j in xrange(height)]
    for i in xrange(height):
        for j in xrange(width):
            if i == 0 and j == 0:
                result[i][j] = grid[i][j]
            elif i == 0:
                result[i][j] = result[i][j-1] + grid[i][j]
            elif j == 0:
                result[i][j] = result[i-1][j] + grid[i][j]
            else:
                result[i][j] = min(result[i][j-1], result[i-1][j]) + grid[i][j]
    return result[height -1][width - 1]

