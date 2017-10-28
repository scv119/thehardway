https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

1. first method is to set first element as minimum and store it in mini. Then compare all the following element with mini, always store minimum element into mini.
This method will take O(n) time complexity and O(1) space complexity.
2. To improve its time complexity, I will use start, middle, end three elements to decide which part this element is in.
as it is originally a sorted array in ascending order, I think about using a O(lgn) method, which will compare the value of middle with start and end. 
this array could be as below:
M1 ... B S ... M0
so there are two parts in this array, M1 to B and S to M0
if start == end, then return nums[start]
if end - start == 1, then return min(nums[start], nums[end])
