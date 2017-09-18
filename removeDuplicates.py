# leetcode: https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

def removeDuplicates(self, nums):
    # time: O(n^2), space: O(1)
    if len(nums) == 0:
        return 0
    num = nums[0]
    i = 1
    while i < len(nums):
        if nums[i] == num:
            nums.pop(i)
        else:
            num = nums[i]
            i += 1
    return len(nums)

def removeDuplicates(self, nums):
    # time: O(n), space: O(1)
    if len(nums) == 0:
        return 0
    length = 0
    num = nums[0]
    i = 1
    while i < len(nums):
        if nums[i] != nums[length]:
            length += 1
            nums[length] = nums[i]
        i = i + 1
    return length + 1
