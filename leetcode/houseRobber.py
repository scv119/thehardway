# leetcode : https://leetcode.com/problems/house-robber/#/description
class Solution(object):
    # solution learned from discussion
    def rob(self, nums):
        """
        : type nums: list[int]
        : rtype: int
        """
        # f(-1) = 0 = preMax, f(0) = 0 = curMax
        # use preMax to hold the max value of n - 2
        # use curMax to hold the max value of n - 1
        # time complexity: O(n), space complexity O(1), we only used extra space: length, temp, cur_max, pre_max
        pre_max = 0
        cur_max = 0
        length = len(nums)
        # f(n) = max(f(n-2) + nums[n], f(n-1))
        # either choose last number or not
        for i in xrange(0, length):
            temp = cur_max
            cur_max = max(pre_max + nums[i], cur_max)
            pre_max = temp
        return cur_max

    # My solution: choose last house or choose penult house:
    # compare last house + max(0 to n - 3 house) and penult house + max(0 to n - 4 house)
    # f(n) = max(f(n-2) + nums[n],  nums[n-1] + f(n-3))
    # time complexity: O(2^n), space complexity is O(n)
    def rob2(self, nums):
        length = len(nums)
        if length == 0:
            return 0
        elif length == 1:
            return nums[0]
        elif length == 2:
            return max(nums[0], nums[1])
        return max(self.rob2(nums[0:length - 2]) + nums[length - 1], self.rob2(nums[0:length - 3])+ nums[length - 2])

    # solution: choose last house or not compare last house + max(0 to n -3 house) and max(0 to n -2) house
    # f(n) = max(f(n-2) + nums[n], f(n-1))
    # time complexity: O(2^n), space complexity is O(n)
    def rob3(self, nums):
        length = len(nums)
        if length == 0:
            return 0
        elif length == 1:
            return nums[0]
        elif length == 2:
            return max(nums[0], nums[1])
        return max(self.rob3(nums[0:length - 2]) + nums[length - 1], self.rob3(nums[0:length - 1]))

solution = Solution()
testList = [183,219,57,193,94,233,202,154,65,240,97,234,100,249,186,66,90,238,168,128,177,235,50,81,185,165,217,207,88,80,112,78,135,62,228,247,211]
print solution.rob(testList)
print solution.rob2(testList)
print solution.rob3(testList)
