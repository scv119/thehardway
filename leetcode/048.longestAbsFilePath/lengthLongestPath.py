# leetcode: https://leetcode.com/problems/longest-absolute-file-path/description/

def lengthLongestPath(self, input):
	# time complexity: O(n), space complexity: O(n), n is the length of input
	dir_list = input.split('\n')
	max_len = 0
	level_len = [0 for i in xrange(len(dir_list) + 1)]
	for dir in dir_list:
		name = dir.lstrip('\t')
		level = len(dir) - len(name)
		if '.' in dir:
			max_len = max(max_len, level_len[level] + len(name))
		else:
			level_len[level + 1] = level_len[level] + len(name) + 1
	return max_len
