# leetcode https://leetcode.com/problems/add-two-numbers/description/

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        : type: l1, l2, ListNode
        : rtype: ListNode
        """
        # time O(n) n is max length of l1 and l2
        carry = False
        cur = head = ListNode(0)
        # attention: [5] + [5], both none but there is a carry
        while l1 != None or l2 != None or carry == True:
            if l1 != None and l2 != None:
                temp_value = l1.val + l2.val
                l1 = l1.next
                l2 = l2.next
            elif l1 != None and l2 == None:
                temp_value = l1.val
                l1 = l1.next
            elif l1 == None and l2 != None:
                temp_value = l2.val
                l2 = l2.next
            else:
                temp_value = 0
            if carry == True:
                temp_value += 1
            if temp_value >= 10:
                temp_value -= 10
                carry = True
            else:
                carry = False
            cur.next = ListNode(temp_value)
            cur = cur.next
        return head.next
