# leetcode: https://leetcode.com/problems/insertion-sort-list/description/

def insertionSortList(self, head):
    # time: O(n^2), space O(1)
    if head == None:
        return None
    new_head = ListNode(0)
    new_head.next = head
    sorted_to = head
    while sorted_to.next != None:
        prev = new_head
        cur = prev.next
        unsort = sorted_to.next
        next_unsort = unsort.next
        unchange = 1
        while cur != unsort:
            if unsort.val > sorted_to.val:
                break
            if unsort.val > cur.val:
                prev = prev.next
                cur = cur.next
            else:
                unchange = 0
                sorted_to.next = next_unsort
                prev.next = unsort
                unsort.next = cur
                break
        if unchange == 1:
            sorted_to = unsort
    return new_head.next
