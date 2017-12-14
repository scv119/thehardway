https://leetcode.com/problems/intersection-of-two-arrays-ii/description/
https://leetcode.com/problems/intersection-of-two-arrays/description/

1. use hashtable: store the first array into hashtable, and check whether the second array's element is in hashtable
time complexity: O(n), space complexity:O(n)
2. sort and compare, sort two arrays, compare these two arrays, if equal, push this element to res array,move two pointers, If not equal, then move one pointer
time complexity: O(nlgn), space complexity: O(n)
follow up:
if this array is already sorted, then method2 is better, time complexity: O(min(n, m)), n is the length of nums1, m is the length of nums2
if nums1's size is small compared to nums2's size, hashtable method is better, store the keys of nums1 into hashtable
if elements of nums2 are stored on disk, then memory is limited such that you cannot load all elements into the memory at once?
if nums1 can fit in memory, then store nums1 into hashtable and read chunks of nums2, and store the intersections
if both cannot fit in memory, then sort these two arrays(external sorting, quicksort + merge sort), then use method2's comparison method.

