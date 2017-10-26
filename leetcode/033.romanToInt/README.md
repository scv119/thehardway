https://leetcode.com/problems/roman-to-integer/description/

from roman to integer
basically the process of converting roman to integer is to add all characters in string. .
Usually sequence of roman number is from big to small.The biggest one will be on the left most position. The smallest one will be on the right most position. But there is an exception.
when left char is smaller than right char, then left char represents a negative value. 
To make it easier to compare, I use a dict to store all the chars as keys and integers they represent as values.
traverse the string, if the left char is smaller than right char, then - left char's value. else, + left char's value. Finally add last char's value and return result

time complexity: O(n), n is the length of string. space complexity: O(1)
