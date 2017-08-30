# leetcode: https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def kthSmallest(self, root, k):
        """
        : type root: TreeNode
        : type k: int
        : rtype: int
        """
        result = self.inorder(root)
        return result[k-1]

    def inorder(self, root):
        if root  == None:
            return []
        return self.inorder(root.left) + [root.val] + self.inorder(root.right)

    def kthSmallest(self, root, k):
        n = self.countNode(root.left)
        if k <= n:
            return self.kthSmallest(root.left, k)
        if k == n + 1:
            return root.val
        if k > n + 1:
            return self.kthSmallest(root.right, k - n - 1)
    def countNode(self, root):
        if root == None:
            return 0
        return 1 + self.countNode(root.left) + self.countNode(root.right)


