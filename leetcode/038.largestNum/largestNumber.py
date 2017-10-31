# leetcode: https://leetcode.com/problems/largest-number/description/

def largestNumber(self, nums):
	res = ""
    compare = lambda a,b:1 if a+b>b+a else -1 if a+b<b+a else 0
    nums = map(str, nums)
    nums.sort(cmp=compare, reverse=True)
    if nums[0] == "0":
        return "0"
    for num in nums:
        res = res + num
    return res
