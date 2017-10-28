# leetcode: https://leetcode.com/problems/bulb-switcher/description/

def bulbswitch(self, n): 
	res = [False for i in xrange(n)]
	for i in xrange(1, n+1):
		j = i - 1
		while j < n:
			res[j] = not res[j]
			j = j + i
	counter = 0
	for i in res:
		if i == True:
			counter += 1
	return counter

def bulbswitch(self, n):
	return int(math.sqrt(n))
