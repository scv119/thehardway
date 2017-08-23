# leetcode https://leetcode.com/problems/symmetric-tree/description/

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        : type root: TreeNode
        : rtype boolean
        """
        # time complexity O(n), space complexity O(1)
        if root == None:
            return True
        return self.helper(root.left, root.right)

    def helper(self, node1, node2):
        if node1 == node2 == None:
            return True
        elif (node1 != None and node2 == None ) or (node1 == None or node2 != None):
            return False
        return self.helper(node1.left, node2.right) and self.helper(node1.right, node2.left)
