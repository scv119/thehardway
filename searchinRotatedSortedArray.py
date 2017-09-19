# leetcode: https://leetcode.com/problems/search-in-rotated-sorted-array/description/

def search(self, nums, target):
    # time: O(n), space: O(1)
    for i in xrange(len(nums)):
        if nums[i] == target:
            return i
    return -1
def search(self, nums, target):
    """
    : type nums: List[int]
    : type target: int
    : rtype: int
    """
    # time: O(lgn), space: O(1)
    length = len(nums)
    if length == 0:
        return -1
    l = 0
    r = length - 1
    while l <= r:
        m = (r + l)/2
        if target = nums[l]:
            return l
        elif target == nums[r]:
            return r
        elif target == nums[m]:
            return m
        elif nums[m] > nums[l]:
            if target > nums[m] or target < nums[l]:
                l = m
            elif target < nums[m] and target > nums[l]:
                r = m
        elif nums[m] < nums[l]:
            if target < nums[m] or target > nums[l]:
                r = m
            elif target > nums[m] and target < nums[l]:
                l = m
        else:
            return -1
