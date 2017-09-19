# leetcode: https://leetcode.com/problems/count-complete-tree-nodes/description/

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(Object):
    def countNodes(self, root):
        """
        : type root: TreeNode
        : rtype: int
        """
        # time: O(n)
        if root == None:
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    def countNodes2(self, root):
        # time: O(lgn*lgn)
        if root == None:
            return 0
        node1 = node2 = root
        left_height = right_height = 0
        while node1:
            left_height = left_height + 1
            node1 = node1.left
        while node2:
            right_height = right_height + 1
            node2 = node2.right
        if left_height == right_height:
            return 2**left_height - 1
        return 1 + self.countNodes2(root.left) + self.countNodes2(root.right)

