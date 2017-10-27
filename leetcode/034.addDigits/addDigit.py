# leetcode: https://leetcode.com/problems/add-digits/description/

# method 1
def addDigits(self, num):
	while len(str(num)) != 1:
		temp = 0
		for i in str(num):
			temp += int(i)
		num = temp
	return num

# method2
def addDigits(self, num):
	if num == 0:
		return 0
	elif num % 9 != 0:
		return num % 9
	else:
		return 9

# method3:
def addDigits(self, num):
	while num >= 10:
		temp = 0
		while num > 0:
			temp += num % 10
			num = num / 10
	return num
