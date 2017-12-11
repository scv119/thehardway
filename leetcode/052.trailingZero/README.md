https://leetcode.com/problems/factorial-trailing-zeroes/description/

to find out the number of trailing zeros, we need to consider what to create a trailing zeros. That is 2 * 5.

1. first method, is to find out how many 2 and how many 5 in [0, n]
	track all number in range (0, n), find out how many 2 and 5 in current number
	get min(counter_5, counter_2)
	it will take O(nlgn) time

2. second method, as there must be more 2 than 5. So I only need to find out how many 5 in all numbers in range(0, n). Logarithmic time complexity gives me a hint. I found out every five numbers can be divided without remainder. So I use n/5. But then for every five there shold be divided without remainder. For example, 25 = 5 * 5. So I will just use n/5, add the result to counter_5 until n < 5. It will take O(lgn) time, space O(1)

3. recursion method: time complexity: O(lgn), space O(lgn)
