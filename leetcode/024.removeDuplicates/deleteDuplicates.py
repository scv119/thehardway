# leetcode: https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/

def deleteDuplicates(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if head == None or head.next == None:
        return head
    prev = head
    cur = head.next
    while cur != None:
        while cur != None and cur.val == prev.val:
        cur = cur.next
        prev.next = cur
        if cur != None:
            prev = cur
            cur = cur.next
    return head
