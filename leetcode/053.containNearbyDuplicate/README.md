https://leetcode.com/problems/contains-duplicate-ii/description/

1. most straight forward method is to compare all numbers in array, if equal, then get the diff between these two numbers' indexes to check whether they are qualified. Time comlexity: O(n^2), space complexity: O(1)

2. use hashtable. Traverse all elements in array from index 0. If this number is not in hashtable, then add this key. Otherwise, compare the index of this element's index with previous index under this key. If the diff is below k, then return True. 
time complexity: O(n), space O(n)
