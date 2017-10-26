# leetcode: https://leetcode.com/problems/roman-to-integer/description/

def romanToInt(self, s):
	table = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
	res = 0
	for i in xrange(len(s) - 1):
		if table[s[i]] < table[s[i+1]]:
			res -= table[s[i]]
		else:
			res += table[s[i]]
	res += table[s[-1]]
	return res
