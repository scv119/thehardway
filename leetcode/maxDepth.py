# leetcode https://leetcode.com/problems/maximum-depth-of-binary-tree/tabs/description
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.right = None
        self.left = None

class Solution(object):
    # recursive solution
    def maxDepth(self, root):
        """
        : type root: TreeNode
        : rtype: int
        """
        # time complexity: O(n), n is the number of all nodes in the tree
        if root == None:
            return 0
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    # iterative BFS solution
    def maxDepth1(self, root):
        if root == None:
            return 0
        queue = [root]
        count = 0
        while len(queue) != 0:
            size = len(queue)
            while size > 0:
                cur = queue.pop(0)
                if cur.left != None:
                    queue.append(cur.left)
                if cur.right != None:
                    queue.append(cur.right)
                size = size - 1
            count = count + 1
        return count

    # iterative DFS solution
    def maxDepth2(self, root)
        if root == None:
            return 0
        stack = [root]
        dep_dict = [1]
        max_dep = 0
        while len(stack) != 0:
            cur = stack.pop()
            while cur.left != None or cur.right != None:
                temp = dep_dict.pop()
                if cur.left != None:
                    stack.append(cur.left)
                    dep_dict.append(temp + 1)
                if cur.right != None:
                    stack.append(cur.right)
                    dep_dict.append(temp + 1)
                cur = stack.pop()
            max_dep = max(max_dep, dep_dict.pop())
        return max_dep

