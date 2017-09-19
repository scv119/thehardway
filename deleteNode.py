# leetcode: https://leetcode.com/problems/delete-node-in-a-linked-list/description/

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteNode(self, node):
        """
        : type node: ListNode
        : rtype: do not return anything, modify node in-place
        """
        # time: O(1)
        node.val = node.next.val
        node.next = node.next.next
