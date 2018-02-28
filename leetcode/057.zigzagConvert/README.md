https://leetcode.com/problems/zigzag-conversion/description/

1					2n - 1
2				2n - 2
3			2n - 3	
.		.
.	.
n

the interval between every char in first line is 2n - 2(n is numRows)

use index of char i

i % interval

if i % interval < numRows:

the element is in the vertical line
the remainder is the line number

else:
the element is in the slant line
interval - remainder is the line number

time O(n), space O(n)
