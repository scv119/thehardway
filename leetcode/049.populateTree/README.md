https://leetcode.com/problems/populating-next-right-pointers-in-each-node/description/

A method: 
1. use BFS to get nodes in level and store it in a list 
2. in this list, each node points to the next 

time complexity: O(n), space complexity: O(n)

Second method:
1. use a variable to track the next level's first child node which will be next level's first root
2. use a variable to traverse all the nodes in the child level 
3, use root to track all the node in the parent level. if root == None, then this level has completed traversal. Then use head to get the next level's first root, and reset head and cur to None.
time complexity: O(n), space complexity: O(1)

