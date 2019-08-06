https://leetcode.com/problems/missing-number/description/

1. XOR: 0 ^ A = A
	A ^ A ^ B = B
   so there is no missing number in array, it will be (0, n+1), index range(0, n + 1). 0 ^ 1 ^ .. ^ n ^ 0 ^ 1 ^ .. ^n will be 0
   if there is a  missing number, index will be (0, n), but one number missing in (0, n+1), then XOR them, the ramaining will be missing number.  
Time: O(n), space: O(1)

