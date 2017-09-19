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
        # time: O(n), space: O(h), n is the number of nodes, h is the height of this tree
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

    def preorderTraversal3(self, root):
        if root == None:
            return []
        result_list = []
        parent = root
        while parent != None:
            if parent.left != None:
                pre = parent.left
                # find most right child node of parent's left node and make it point to parent node
                # if it already points to parent node, it means we have already finished left part, then release the relationship and move on to right node of parent
                while pre.right != None and pre.right != parent:
                    pre = pre.right
                if pre.right == None:
                    result_list.append(parent.val)
                    pre.right = parent
                    parent = parent.left
                else:
                    pre.right = None
                    parent = parent.right
            # parent has no left node, then append parent value and moves on to right node of parent
            else:
                result_list.append(parent.val)
                parent = parent.right
        return result_list
