# leetcode https://leetcode.com/problems/3sum/#/discuss

class Solution(object):
    def threeSum(self, nums):
        """
        : type nums: List[int]
        : rtype: List[List[int]]
        """
        # O(nlgn)
        nums.sort()
        result = []
        # O(n^2) time complexity, space complexity is O(1) if result is not considered as extra space.
        for i in xrange(0, len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                tempSum = nums[i] + nums[l] + nums[r]
                if tempSum < 0:
                    l = l + 1
                elif tempSum > 0:
                    r = r - 1
                else:
                    result.append([nums[i], nums[l], nums[r]])
                    # skip same values
                    while l < r and nums[l] == nums[l + 1]:
                        l = l + 1
                    while l < r and nums[r] == nums[r - 1]:
                        r = r - 1
                    l = l + 1
                    r = r - 1
        return result

solution = Solution()
testList = [2, -1, 1, 0, 0, -2]
result = solution.threeSum(testList)
print result

