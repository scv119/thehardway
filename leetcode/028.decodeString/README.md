https://leetcode.com/problems/decode-string/description/

use stack to track it
if this char is a digit, then calculate the index until it reaches "["
if it is a "[", push index onto stack
if it is a - z, then push onto stack
if it is a "]", then pop get the latest k[] string and push this string on stack
time complexity: O(n), space complexity: O(n)

