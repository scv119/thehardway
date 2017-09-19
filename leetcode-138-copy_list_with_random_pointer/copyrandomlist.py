# leetcode: https://leetcode.com/problems/copy-list-with-random-pointer/description/

class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.randome = None


class Solution(object):
    # time: O(n), space: O(n), n is the number of list nodes
    def copyRandomList(self, head):
        if head == None:
            return None

        # copy all nodes with next information, put duplicated node after the original ones
        cur = head
        while cur != None:
            new_node = RandomListNode(cur.label)
            next_node = cur.next
            cur.next = new_node
            new_node.next = next_node
            cur = next_node

        # copy all random node relations
        # we cannot separate original list from copy list as it may lead to erros when one node randomly points to a previous node and separation make it impossible to locate the correct node.
        cur = head
        while cur != None:
            new_node = cur.next
            if cur.random != None:
                new_node.random = cur.random.next
            cur = new_node.next

        # separte copy list from original list
        new_cur = new_link = RandomListNode(0)
        cur = head
        while cur != None:
            new_node = cur.next
            new_cur.next = new_node
            cur.next = new_node.next
            cur = cur.next
            new_cur = new_node
        new_cur.next = None

        return new_link.next
