# leetcode: https://leetcode.com/problems/missing-number/description/

def missingNumber(self, nums):
	result = 0
	for i in xrange(len(nums)):
		result = result ^ nums[i] ^ i
	return result ^ len(nums)
