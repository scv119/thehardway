# leetcode: https://leetcode.com/problems/remove-linked-list-elements/description/

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    # time: O(n), space O(1)
    def removeElements(self, head, val):
        result = prev = ListNode(0)
        prev.next = head
        while head != None:
            if head.val == val:
                prev.next = head.next
                head = head.next
            else:
                head = head.next
                prev = prev.next
        return result.next
