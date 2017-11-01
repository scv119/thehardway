# leetcode: https://leetcode.com/problems/set-matrix-zeroes/description/

def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)
        first_row = 1
        first_col = 1
        for i in xrange(0, length):
            if matrix[i][0] == 0:
                first_col = 0
        for j in xrange(0, len(matrix[0])):
            if matrix[0][j] == 0:
                first_row = 0
        for i in xrange(1, length):
            for j in xrange(1,len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in xrange(1, length):
            for j in xrange(1, len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if first_row == 0:
            for j in xrange(len(matrix[0])):
                matrix[0][j] = 0
        if first_col == 0:
            for i in xrange(length):
                matrix[i][0] = 0
