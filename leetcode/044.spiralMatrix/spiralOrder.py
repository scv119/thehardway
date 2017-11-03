# leetcode: https://leetcode.com/problems/spiral-matrix/description/


def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0:
            return []
        res = []
        cols = len(matrix[0])
        rows = len(matrix)
        row_start = 0
        row_end = rows
        col_start = 0
        col_end = cols
        num = 0
        k = 0
        while num < cols * rows:
            if k % 4 == 0:
                for i in xrange(col_start, col_end):
                    res.append(matrix[row_start][i])
                    num += 1
                row_start += 1
                k += 1
            elif k % 4 == 1:
                for i in xrange(row_start, row_end):
                    res.append(matrix[i][col_end-1])
                    num += 1
                col_end -= 1
                k += 1
            elif k % 4 == 2:
                for i in xrange(col_end - 1, col_start - 1, -1):
                    res.append(matrix[row_end-1][i])
                    num += 1
                row_end -= 1
                k += 1
            elif k % 4 == 3:
                for i in xrange(row_end - 1, row_start - 1, -1):
                    res.append(matrix[i][col_start])
                    num += 1
                col_start += 1
                k += 1
        return res
