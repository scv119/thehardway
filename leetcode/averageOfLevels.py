# leetcode: https://leetcode.com/problems/average-of-levels-in-binary-tree/description/

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def averageOfLevels(self, root):
        # time O(n) space O(n)
        # BFS
        if root == None:
            return []
        result = []
        queue = [root]
        while len(queue) != 0:
            sum_result = 0
            count = 0
            temp = []
            for i in queue:
                sum_result = sum_result + i.val
                count = count + 1
                if i.left != None:
                    temp.append(i.left)
                if i.right != None:
                    temp.append(i.right)
            result.append(sum_result/float(count))
            queue = temp
        return result

