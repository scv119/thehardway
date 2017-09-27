# leetcode: https://leetcode.com/problems/add-two-numbers-ii/description/

def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        stack1 = []
        while l1 != None:
            stack1.append(l1.val)
            l1 = l1.next
        stack2 = []
        while l2 != None:
            stack2.append(l2.val)
            l2 = l2.next
        carry = 0
        next_node = None
        while len(stack1) != 0 or len(stack2) != 0:
            tempSum = 0
            if len(stack1) != 0:
                tempSum = tempSum + stack1.pop()
            if len(stack2) != 0:
                tempSum = tempSum + stack2.pop()
            if carry != 0:
                tempSum += 1
            if tempSum >= 10:
                carry = 1
            else:
                carry = 0
            tempSum = tempSum % 10
            new_list = ListNode(tempSum)
            new_list.next = next_node
            next_node = new_list
        if carry == 1:
            new_list = ListNode(1)
            new_list.next = next_node
        return new_list


def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        value1 = 0
        while l1 != None:
            value1 = value1 * 10  + l1.val
            l1 = l1.next
        value2 = 0
        while l2 != None:
            value2 = value2 * 10 + l2.val
            l2 = l2.next
        value = value1 + value2
        if value == 0:
            return ListNode(0)
        next_node = None
        while value != 0:
            digit = value % 10
            new_node = ListNode(digit)
            new_node.next = next_node
            next_node = new_node
            value = (value - digit) / 10
        return new_node
