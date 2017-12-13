https://leetcode.com/problems/rotate-array/description/

1. if not modify it in place, then I can make a copy of this list, and use (i + k) % len(nums) to get the new index and change the value on that position, time: O(n), space: O(n)

2. make use of reverse method, reverse the entire list, then reverse the first (0:k), then reverse the remaining. time: O(n), space: O(1)

3. I try to store the previous value into a variable, get to be changed position and replace it with previous value
   At first, I did not consider conditions that there might be a couple of cycles.
   So I have to use a counter to track whether all positions are replaced.
   time O(n), space O(1)
	



