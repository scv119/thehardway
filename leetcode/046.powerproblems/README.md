https://leetcode.com/problems/power-of-three/description/
https://leetcode.com/problems/power-of-two/description/
https://leetcode.com/problems/power-of-four/description/

check a number is a power of a specific number
power of three
power of two
power of four

first check whether n > 0

1, iterative method, use a variable to track every number which is a power of 3 until find the target number or being bigger than the target number.
Time complexity: O(lgn), space complexity：O（1）
n is the target number

2, convert decimal to base 2, 3, 4
   all these converted string shall be like 10000...
time complexity: O(lgn), space complexity: O(lgn)

3. bit manipulation
like for power of 2: whether x is a power of 2  
x in binary will be "00001000..."
x - 1 will be "00000111111..."
x & (x-1) will be "000000"
for power of 4, x
x in binary will be "..100"
1 will always be on the 1st, 3rd, 5th position 
x & 1010101010101010101010101010101 will be only keep the 1 bit x has, so it will be equal to x  
Then we have to exclude the power of 2
the choice of number will depend on the range.
power of 3, 3 is a prime number, the only divisor of 3^19 will be 3^0, 3^1, 3^2
FOR THIS KIND of solution, time complexity is O(1), space complexity: O(1)
so use a max int which is a power of 3 m, m % x, if m % x == 0, then x is a power of 3.
