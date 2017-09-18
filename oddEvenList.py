# leetcode: https://leetcode.com/problems/odd-even-linked-list/description/

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    # time complexity O(n), space complexity O(1)
    def oddEvenList(self, head):
        if head == None:
            return None
        list1 = odd = ListNode(0)
        list2 = even = ListNode(0)
        while head:
            odd.next = head
            even.next = head.next
            odd = odd.next
            even = even.next
            if even != None:
                head = head.next.next
            else:
                break
        odd.next = list2.next
        return list1.next
