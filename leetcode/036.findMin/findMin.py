# leetcode: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

def findMin(self, nums):
	mini = nums[0]
	for i in xrange(1, len(nums)):
		mini = min(nums[i], mini)
	return mini

def findMin(self, nums):
	start = 0
    end = len(nums) - 1
    while end >= start:
        if start == end:
            return nums[start]
        if end - start == 1:
            return min(nums[start], nums[end])
        mid = start + (end - start) / 2
        if nums[mid] > nums[start] and nums[mid] > nums[end]:
            start = mid
        elif nums[mid] < nums[start] and nums[mid] < nums[end]:
            end = mid
        elif nums[mid] > nums[start] and nums[mid] < nums[end]:
            end = mid
        elif nums[mid] > nums[start] and nums[mid] > nums[end]:
            start = mid
