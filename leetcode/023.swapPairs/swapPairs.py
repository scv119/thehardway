#leetcode: https://leetcode.com/problems/swap-nodes-in-pairs/description/

def swapPairs(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    # time: O(n), space: O(1)
    if head == None or head.next == None:
        return head
    res = pre = ListNode(0)
    res.next = head
    pair1 = head
    pair2 = head.next
    while pair1 != None and pair2 != None:
        tempNext = pair2.next
        pre.next = pair2
        pair2.next = pair1
        pair1.next = tempNext
        pre = pair1
        if pair1.next == None:
            break
        else:
            pair1 = pair1.next
            pair2 = pair1.next
    return res.next

def swapPairs(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    # time: O(n), space: O(n)
    if head == None or head.next == None:
        return head
    pair1 = head
    pair2 = head.next
    pair1.next = self.swapPairs(pair2.next)
    pair2.next = pair1
    return pair2
