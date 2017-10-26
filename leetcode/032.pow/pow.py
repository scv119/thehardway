# leetcode: https://leetcode.com/problems/powx-n/description/

# method 1: O(n) time complexity, O(1) space complexity
def myPow(self, x, n):
    if n == 0:
       return 1
    res = 1
    for i in xrange(abs(n)):
       res * = x
    if n < 0:
       return 1.0/res
    return res

# method2: O(lgn) time complexity, O(lgn) space complexity
def myPow(self, x, n):
	if n == 0:
	power = abs(n)
	res = sefl.helper(x, power)
	if n < 0:
		return 1.0/res
	return res

def helper(self, x, n):
	if n == 1:
		return x
	elif n % 2 == 0:
		temp = self.helper(x, n/2)
		return temp * temp
	else:
		temp = self.helper(x, (n-1)/2)
		return temp * temp * x

# method3: time complexity shall between O(n) and O(lgn), O(1) space complexity
def myPow(self, x, n):
	if n == 0:
		return 1
	i = 1
	res = x
	power = abs(n)
	while 2 * i <= power:
		i = i * 2
		res = res * x
	while i < power:
		i += 1
		res = res * x
	if n < 0:
		return 1.0/res
	return res

