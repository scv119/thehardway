https://leetcode.com/problems/largest-number/description/

1. convert nums to string list for sorting purpose.
2. make use of sort() function to compare strings in list.
   compare rule:
   "12" "3"
   "123" < "312"
   so "3" is always before "12"
   I learned sort(compare function, reverse=True)
   define lambda function
   lambda a, b(parameters):(return value)1 if a+b < b+a else -1 if a+b > b+a else 0
   oneline if elif else statement
   1 if a+b<b+a else -1 if a+b >b+a else 0
   if a+b <  b+a:
     return 1
   elif a +b > b+a:
     return -1
   else
     return 0
3. concatenate the sorted string list

4, attention: if sorted string's first is "0", then return "0" rather than "000"

space complexity O(n)
time complexity O(nklgnk), n is the length of list, k is the length of strings
