# leetcode https://leetcode.com/problems/path-sum/description/

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def hasPathSum(self, root, sum):
        """
        : type root: TreeNode, sum: int
        : rtype: boolean
        """
        # time: O(n), space: O(1)
        if root == None:
            return False
        sum = sum - root.val
        if root.left == None and root.right == None and sum == 0:
            return True
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)
