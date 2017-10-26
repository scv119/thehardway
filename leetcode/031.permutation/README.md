https://leetcode.com/problems/permutations/description/

think about when there is only number in list, possible permutations is only [[1]]
if I add another number 2, then there are two types, add 2 in front of 1 or after 1, which will be [[1, 2], [2, 1]]
if I add another number 3, then I can insert 3 into space of previous lists. [[1, 2, 3], [3, 1, 2], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1]] 
so If I add another number 4.
for each list in the above list:
_number_number_number_, I will put the new number into the _ space
So I used one helper function to add new number and return new list.

helper function:
traverse all the list:
	make a copy of this list
	traverse all the positions(0 to len(list))
		insert this new number into this position
		append this new list into result list
return the resultlist

permute function:
	put first number into resultList
	use helper function to add other numbers

time complexity: O(n^4), space complexity: O(n!)



	

