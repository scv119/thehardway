# leetcode: https://leetcode.com/problems/plus-one-linked-list/description/

def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        stack = []
        cur = head
        while cur != None:
            stack.append(cur.val)
            cur = cur.next
        carry = 0
        last = stack.pop()
        if last + 1 < 10:
            next_node = new_node = ListNode(last + 1)
            carry = 0
        else:
            next_node = new_node = ListNode(last + 1 - 10)
            carry = 1
        while len(stack) != 0:
            if carry == 1:
                temp = stack.pop() + 1
            else:
                temp = stack.pop()
            if temp >= 10:
                carry = 1
                temp = temp - 10
            else:
                carry = 0
            new_node = ListNode(temp)
            new_node.next = next_node
            next_node = new_node
        if carry == 1:
            new_node = ListNode(1)
            new_node.next = next_node
        return new_node


def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        last_not_9 = dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        while cur != None:
            if cur.val != 9:
                last_not_9 = cur
            cur = cur.next
        last_not_9.val += 1

        cur = last_not_9.next
        while cur != None:
            cur.val = 0
            cur = cur.next
        if dummy.val != 0:
            return dummy
        return head
