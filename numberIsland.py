# leetcode: https://leetcode.com/problems/number-of-islands/#/description
class Solution(object):
    def numIslands(self, grid):
        """
        : type grid: List[List[str]]
        : rtype: int
        """
        # time complexity is O(mn), m = row number, n = col number, as every point will be visited once
        if grid == []:
            return 0
        num = 0
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                # if one island found, increase counter num and use helper function to mark all connected island grid
                if grid[i][j] == "1":
                    num += 1
                    self.helper(grid, i, j)
        return num

    # this helper function is used to mark all connected grid on island  with "*"
    def helper(self, grid, i, j):
        grid[i][j] = "*"
        row = len(grid)
        col = len(grid[0])
        if i - 1 >= 0:
            if grid[i - 1][j] == "1":
                self.helper(grid, i - 1, j)
        if j - 1 >= 0:
            if grid[i][j - 1] == "1":
                self.helper(grid, i, j - 1)
        if i + 1 < row:
            if grid[i + 1][j] == "1":
                self.helper(grid, i + 1, j)
