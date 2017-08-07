# leetcode:  https://leetcode.com/problems/binary-tree-preorder-traversal/description/

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def preorderTraversal(self, root):
        """
        :rtype: List[int]
        """
        # time: O(n), space: O(1) if not consider return list
        if root == None:
            return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)

    def preorderTraversal2(self, root):
        # iterative
        # time: O(n), space: O(n)
        if root == None:
            return []
        result_list = []
        stack = [root]
        while len(stack) != 0:
            temp = stack.pop()
            result_list.append(temp.val)
            if temp.right != None:
                stack.append(temp.right)
            if temp.left != None:
                stack.append(temp.left)
        return result_list
