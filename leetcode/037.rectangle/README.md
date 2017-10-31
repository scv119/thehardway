https://leetcode.com/problems/rectangle-area/description/

1, calculate area of each rectangle and delete overlapped area if there is an overlap. Time O(1) Space O(1)
2,no overlap: rectangle1's x range is out of rectangle2's x range or rectangle1's y range is out of rectangle2's y range.
3, overlapped area: choose max(smaller x value), min(bigger x value), max(smaller y value), min(bigger y value)
	
