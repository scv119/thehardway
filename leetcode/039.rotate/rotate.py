# leetcode: https://leetcode.com/problems/rotate-image/description/


def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)
        for i in xrange(length/2):
            for j in xrange(length):
                matrix[i][j], matrix[length - 1 - i][j] = matrix[length - 1 - i][j], matrix[i][j]
        for i in xrange(length):
            for j in xrange(i+1):
                if i != j:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
