https://leetcode.com/problems/bulb-switcher/description/

1. first method:
 use a table to track the status of all bulbs
 for i in 1 to n:
    change i * k bulb's status
 use a counter to track bulb which is on

time complexity: O(n ^ 2), space complexity: O(n)

2. second method:
find all bulb whose status is on are on the position of square index, such as 1, 4, 9...
for all bulbs, toggle time shall be a odd number. For example, the fourth bulb, it will be toggled at 1, 2, 4.
for all bulbs except squares, they will be toggled for a even number times.
Like 3 = 1 * 3, will be toggled at 1, 3
Like 5 = 1 * 5, will be toggled at 1, 5
Like 6 = 1 * 2 * 3, will be toggled at 1, 2, 3, 6
all these numbers can be expressed as a * b * c * d * ....( a, b, c, d are prime numbers)
they will be toggled for even times n(n-1)*...*1 
Time complexity: O(1), space complexity: O(1)

