https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/

use pre and cur to track the value if cur's value is equal to pre's value, then cur points to next, until cur's value is different or cur is None 
if cur's value is not equal to pre's value, then pre.next = cur if cur is not None, then make pre to be cur, cur to be pre's next. 
And continue compare pre's and cur's values 
time complexity is O(n) and space complexity is O(1)
