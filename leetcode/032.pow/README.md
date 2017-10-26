https://leetcode.com/problems/powx-n/description/

First method is to use O(n) running time. But obviously there are O(lgn) running time method. But it may sacrify some memory. It will take O(lgn) space complexity.

1. if use O(n) time, O(1) space, n is the power number. 
	consider when n < 0, n > 0 and n = 0, different result 

2. use O(lgn) time O(lgn) space
	myPow(x, n) = myPow(x, n/2) ^ 2
	But we need to consider when n % 2 == 0 and n % 2 != 0
	it is a resursive solution. I tried to do it iteratively but it seems need to take O(lgn) or more space.

3. use a variable to check what is the biggest 2 ^ i <= power, mutiply x for i times
   if 2 ^ i < power number, then continue mutiply x for (n - 2 ^i) times. The best result is when 2 ^ i == n, it will be O(lgn) time complexity. But with n increasing, the result will get worse. I do not know how to calculate the time complexity, it shall be between O(lgn) and O(n). 
