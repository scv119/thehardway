#leetcode: https://leetcode.com/problems/swap-nodes-in-pairs/description/

def swapPairs(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    # time: O(n), space: O(1)
    if head == None or head.next == None:
        return head
    sentry = pre = ListNode(0)
    sentry.next = head
    first = head
    second = head.next
    while first != None and second != None:
        tempNext = second.next
        pre.next = second
        second.next = first
        first.next = tempNext
        pre = first
        if first.next == None:
            break
        else:
            first = pair1.next
            second = first.next
    return sentry.next

def swapPairs(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    # time: O(n), space: O(n)
    if head == None or head.next == None:
        return head
    first = head
    second = head.next
    first.next = self.swapPairs(second.next)
    second.next = first
    return second
