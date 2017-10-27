https://leetcode.com/problems/add-digits/description/

1. convert number into string 
   while string's length is not 1
       convert char in string into int
       add all ints in string
       store sum to number
       convert number into string

2. use O(1) time, O(1) space 
   number = (100 * a + 10 * b + c) 
   number % 9 = (99a + a + 99b + b + c) % 9 = (a + b + c) % 9
   if number % 9 == 0:
      result = 9
   else:
     result = number % 9
   one exception is when number = 0, result = 0  

3. while num >= 10:
	add all digit in number
	use mod method
        store sum into num
O(1) space, I do not know how to calculate the time complexity


        
