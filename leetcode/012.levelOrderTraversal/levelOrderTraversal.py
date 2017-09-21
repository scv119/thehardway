# leetcode https://leetcode.com/problems/binary-tree-level-order-traversal/description/

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrder(self, root):
        """
        : type root: TreeNode
        : rtype: List[List[int]]
        """
        # time complexity: O(n), space complexity: O(n)
        if root == None:
            return []
        result = [[root.val]]
        queue = [root]
        while len(queue) != 0:
            temp = []
            tempList = []
            for node in queue:
                if node.left != None:
                    temp.append(node.left.val)
                    tempList.append(node.left)
                if node.right != None:
                    temp.append(node.right.val)
                    tempList.append(node.right)
            queue = tempList
            if temp != []:
                result.append(temp)
        return result
