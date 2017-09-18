# leetcode https://leetcode.com/problems/reverse-linked-list/description/

def reverseList(self, head):
    """
    : type head: ListNode
    : rtype: ListNode
    """
    if head == None or head.next == None:
        return head
    prev = head
    cur = head.next
    nex = head.next.next
    while nex != None:
        cur.next = prev
        head.next = nex
        prev = cur
        cur = nex
        nex = nex.next
    head.next = None
    cur.next = prev
    return cur

def reverseList(self, head):
    if head == None or head.next == None:
        return None
    temp = self.reverseList(head.next)
    head.next.next = head
    head.next = None
    return temp

