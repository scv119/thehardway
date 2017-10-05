#https://leetcode.com/problems/minimum-absolute-difference-in-bst/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        min_diff = float("inf")
        stack = []
        prev = -1
        while stack != [] or root != None:
            while root != None:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if min_diff == float("inf") and prev == -1:
                prev = root.val
            else:
                min_diff = min(root.val - prev, min_diff)
                prev = root.val
            root = root.right
        return min_diff
