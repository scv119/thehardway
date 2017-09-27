https://leetcode.com/problems/add-two-numbers-ii/description/

add two numbers in linked list in reverse order, store the result in a new linkedlist

1. traversal the linked list and calculate the number of each linked list. Then store the sum into a new linked list. In this condition, we may need to think about overflow

2. traversal the linked lists and store vals in each node into stacks. Then pop element from stack and add them up. PAY ATTENTION:!!!! last digit may be a carry even though linked list is empty

method1: time: O(n), space: O(1)
method2: time: O(n), space: O(n)
