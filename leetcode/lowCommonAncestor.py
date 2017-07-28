# leetcode : https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/tabs/description/

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        : type root: TreeNode
        : type p: TreeNode
        : type q: TreeNode
        : rtype: TreeNode
        """
        # time complexity is O(n), n is the height of tree
        # recursive method
        # remember: BST character: left val < root val < right val
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root

    def lowestCommonAncestor2(self, root, p, q):
        # iterative method
        while root != None:
            if p.val < root.val and q.val < root.val:
                root = root.val
            elif q.val > root.val and q.val > root.val:
                root = root.val
            else:
                return root
