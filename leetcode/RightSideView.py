# leetcode: https://leetcode.com/problems/binary-tree-right-side-view/description/

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def rightSideView(self, root):
        """
        : rtype: List[int]
        """
        # time: O(n), space O(m)
        if root == None:
            return []
        queue = [root]
        result = []
        while len(queue) != 0:
            result.append(queue[-1].val)
            temp = []
            for i in queue:
                if i.left != None:
                    temp.append(i.left)
                if i.right != None:
                    temp.append(i.right)
            queue = temp
        return result
