https://leetcode.com/problems/minimum-absolute-difference-in-bst/description/

to find out the minimum absolute difference between any nodes in a BST, the most straight forward way is to traversal the BST in inorder. Then the result will be a list in an increasing order. Then find out the minimum diff between every two adjacent values in this list. 
remember BST is a tree that every left node's value is less than its parent node and this parent node's value is less than its right node' value.
Time complexity: O(n), Space complexity: O(n)
