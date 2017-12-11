# leetcode: https://leetcode.com/problems/factorial-trailing-zeroes/description/

def trailingZeroes(self, n):
	counter_5 = 0
	while n >= 5:
		n = n / 5
		counter_5 += n
	return counter_5


def trailingZeroes(self, n):
	counter_2 = 0
	counter_5 = 0
	for i in xrange(2, n+1):
		temp = i
		while temp % 2 == 0:
			temp = temp / 2
			counter_2 += 1
		temp = i
		while temp % 5 == 0:
			temp = temp / 5
			counter_5 += 1
	return min(counter_2, counter_5)

def trailingZeroes(self, n):
	if n == 0:
		return 0	
	else:
		return n / 5 + self.trailingZeroes(n / 5)
