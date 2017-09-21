# leetcode: https://leetcode.com/problems/intersection-of-two-linked-lists/#/description

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        : type headA, headB: ListNode
        : rtype: ListNode
        """
        # time complexity: O(n) and space complexity is O(1)
        n = m = 0
        tempA, tempB = headA, headB
        while tempA != None:
            n += 1
            tempA = tempA.next
        while tempB != None:
            m +=1
            tempB = tempB.next
        if m > n:
            diff = m - n
            for i in xrange(diff):
                headB = headB.next
        else:
            diff = n - m
            for i in xrange(diff):
                headA = headA.next
        while headA != None and headB != None:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None

