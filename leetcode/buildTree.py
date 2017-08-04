# leetcode: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        : type preorder: List[int]
        : type inorder: List[int]
        : retype: TreeNode
        """
        # time: O(n^2)
        if len(inorder) == O:
            return None
        ind = inorder.index(preorder.pop(0))
        root = TreeNode(inorder[ind])
        root.left = self.buildTree(preorder, inorder[0:ind])
        root.right = self.buildTree(preorder, inorder[ind+1:]
        return root
