# leetcode: https://leetcode.com/problems/shortest-unsorted-continuous-subarray/description/

def findUnsortedSubarray(self, nums):
    # time: O(n), space: O(1)
    left = 0
    right = len(nums) - 1
    start = left
    end = right
    while left < right and nums[left] >= nums[start]:
        start = left
        left = left + 1
    if left == right and nums[left] >= nums[start]:
        return 0
    while right > start and nums[right] <= nums[end]:
        if nums[right] != nums[end]:
            end = right
        right = right - 1
    return end - start + 1
