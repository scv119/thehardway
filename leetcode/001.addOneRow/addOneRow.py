# leetcode: https://leetcode.com/problems/add-one-row-to-tree/description/

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def addOneRow(self, root, v, d):
        """
        : type root TreeNode, v, d int
        : rtype TreeNode
        """
        # time: O(n) space: O(n)
        if d == 1:
            new_root = TreeNode(v)
            new_root.left = root
            return new_root
        queue = [root]
        j = 1
        while len(queue) != 0 and j < d - 1
            temp = []
            for i in queue:
                if i.left != None:
                    temp.append(i.left)
                if i.right != None:
                    temp.append(i.right)
            queue = temp
            j = j + 1
        for i in queue:
            temp_left = i.left
            temp_right = i.right
            i.left = TreeNode(v)
            i.left.left = temp_left
            i.right = TreeNode(v)
            i.right.right = temp_right
        return root

    def addOneRow2(self, root, v, d):
        # time O(n) space O(1)
        if d == 0 or d == 1:
            new_root = TreeNode(v)
            if d == 1:
                new_root.left = root
            elif d == 0:
                new_root.right = root
            return new_root
        if d > 1 and root != None:
            if d > 2:
                root.left = self.addOneRow2(root.left, v, d - 1)
                root.right = self.addOneRow2(root.right, v, d - 1)
            elif d == 2:
                root.left = self.addOneRow2(root.left, v, 1)
                root.right = self.addOneRow2(root.right, v, 0)
        return root
