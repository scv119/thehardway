# leetcode: https://leetcode.com/problems/kth-largest-element-in-an-array/description/ 

def findKthLargest(self, nums, k):
    sort(nums, reverse=True)
    return nums[k-1]

