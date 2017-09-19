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


