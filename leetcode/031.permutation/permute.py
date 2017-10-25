# leetcode: https://leetcode.com/problems/permutations/description/

# first solution
    def	permute(self, nums):
    	"""
    	:type nums: List[int]
    	:rtype: List[List[int]]
    	"""
	length = len(nums)
	temp_list = [[nums[0]]
	for i in xrange(1, length):
		temp_list = self.helper(temp_list, nums[i])
	return temp_list

   def  helper(self, num_lists, new_num):
	res = []
	for num_list in num_lists:
		for i in xrange(len(num_list) + 1):
			temp = list(num_list)
			temp.insert(i, new_num)
			res.append(temp)
	return res

	
#modification:
   def 	helper(self, num_lists, new_num):
	res = []
	for num_list in num_lists:
		for i in xrange(len(num_list) + 1):
			res.append(num_list[:i] + [new_num] + num_list[i:])
	return res


