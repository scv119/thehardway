https://leetcode.com/problems/power-of-three/description/

def isPowerOfThree(self, n):
	# time complexity: O(1), space complexity: O(1)
	return n > 0 and 1162261467 % n == 0

def isPowerOfThree(self, n):
	# time complexity: O(lgn), space complexity: O(1)
	i = 1
        while i <= n:
            if i == n:
                return True
            i = i * 3
        return False
	
	
