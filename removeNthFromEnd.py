# leetcode: https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

def removeNthFromEnd(self, head, n):
    # time: O(m), space O(1), m is the length of the linked list
    new_list = prev = ListNode(0)
    prev.next = head
    slow = fast = head
    i = 1
    while i < n:
        fast = fast.next
        i = i + 1
    while fast.next != None:
        fast = fast.next
        slow = slow.next
        prev = prev.next
    next_node = slow.next
    prev.next = next_node
    return new_list.next
