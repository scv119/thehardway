https://leetcode.com/problems/spiral-matrix/description/

1. my thought:
   traverse the matrix in spiral order, always in the order of first row, last col, last row, first col. Every time finish one row or one col, the remaining cols or rows will be affected. So I just change the start row index or the start col index or the end row index or the end col index.
So I used four boolean variable to track the order 
To track the end of traversal, I use a variable called num to track length of result list. When it is less than total element number in matrix, then continue.
Space complexity is O(mn), time complexity is O(mn)
