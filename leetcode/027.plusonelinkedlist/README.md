https://leetcode.com/problems/plus-one-linked-list/description/

1. method1: use stack to store digits and pop them to add 1 if necessary, time complexity: O(n), space complexity: O(n)

2. method2: use last_not_9 to track the last not 9 digit, if the following are all 9, then add 1 will make them to be 0, carry 1 to the previous digit.
so we find last_not_9 node and add 1 to its value, then make all the following not None node's value to be 0. The tricky thing is to add dummy node at the beginning in case carry 1 to increase one digit.
time complexity: O(n), space complexity: O(1)
