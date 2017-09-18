# leetcode: https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/description/

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Solution(object):
    # time: O(n) n is the number of nodes, space O(n)
    def sortedListToBST(self, head):
        val_list = []
        while head != None:
            val_list.append(head.val)
            head = head.next
        return self.listToBST(val_list)


    def listToBST(self, value_list):
        length = len(value_list)
        if length == 0:
            return None
        root = TreeNode(value_list[length/2])
        root.left = self.listToBST(value_list[0:length/2])
        root.right = self.listToBST(value_list[length/2+1:])
        return root

