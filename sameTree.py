# leetcode: https://leetcode.com/problems/same-tree/tabs/description/
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        : type p: TreeNode
        : type q: TreeNode
        : rtype: bool
        """
        # time complexity: O(n), n is the min(number of p, number of q)
        # recursive method
        if p == None and q == None:
            return True
        elif p == None or q == None:
            return False
        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False

    # iterative method
    def isSameTree(self, p, q):
        if p == None and q == None:
            return True
        elif p == None or q == None:
            return False
        pstack = [p]
        qstack = [q]
        while len(pstack) != 0 and len(qstack) != 0:
            cur_p = pstack.pop()
            cur_q = qstack.pop()
            if cur_p.val != cur_q.val:
                return False
            if cur_p.left != None:
                cur_p.append(cur_p.left)
            if cur_q.left != None:
                cur_q.append(cur_q.left)
            if len(pstack) != len(qstack):
                return False
            if cur_p.right != None:
                cur_p.append(cur_p.right)
            if cur_q.right != None:
                cur_q.append(cur_q.right)
            if len(pstack) != len(qstack):
                return False
        return True


