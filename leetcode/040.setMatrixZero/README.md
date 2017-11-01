https://leetcode.com/problems/set-matrix-zeroes/description/

1. first method:
   traverse the 2d array to find out all the rows and all the cols that should be 0.
   use two list to record all the rows and all the cols that have 0.
   This method will use O(m+n) space complexity, m is the row length, n is the column length
   time complexity will be O(m*n*(m+n)), as traverse 2d array will cost O(n*m) and find out whether one row or col is in the list cost O(m+n) time
   
2. second method:
   to improve space complexity, I will use sth to record the rows and the cols that should be 0.
   My first idea is to use set first of row and first of col to be 0.  
   And I still need two variable to track whether first row and first col shall be 0 as if I use first row and first col to record then whether first row and first col shall be 0 cannot be decided. So I think about traverse the first row and first col to check whether they will be 0.
  Then traverse all the other lines and if there is a zero, then set the corresponding first row and first col to be 0.
  Then traverse all lines except first row and first col, set all the lines that should be 0 to be 0.
  Then check whether first row and first col are 0 and change the value of them.
  Time complexity is O(n*m), Space complexity is O(1)
  

