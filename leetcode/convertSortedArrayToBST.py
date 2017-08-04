# leetcode https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        : type: nums: List[int]
        : rtype: TreeNode
        """
        # runtime complexity: O(n)  n is the length of list, as it will walk through every number in nums. Len() function is O(1) time complexity and other execution are all O(1).
        # space complexity O(1). List slicing does not make a new copy of list. Instead it just copies the reference to these elements.
        # reference: https://stackoverflow.com/questions/5131538/slicing-a-list-in-python-without-generating-a-copy
        if len(nums) == 0:
            return None
        mid = len(nums) / 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[0:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root
