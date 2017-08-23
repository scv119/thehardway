# leetcode: https://leetcode.com/problems/single-element-in-a-sorted-array/#/description

class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        : type nums: List[int]
        : rtype: int
        """
        # requirement: time complexity: O(lgn), space complexity: O(1)
        # first thought is to track mid point and compare
        start = 0
        end = len(nums) - 1
        while start <= end:
            if start == end:
                return nums[start]
            else:
                mid = start + (end - start)/2 + 1
                # from start to mid there are odd number of elements
                if (mid - start) % 2 == 0:
                    if nums[mid] == nums[mid - 1]:
                        end = mid - 2
                    else:
                        start = mid
                # from start to mid there are even number of elements
                else:
                    if nums[mid] == nums[mid - 1]:
                        start = mid + 1
                    else:
                        end = mid - 1

solution = Solution()
testList = [3, 3, 7, 7, 10, 11, 11]
testList2 = [3, 3, 5, 7, 7, 11, 11]
result = solution.singleNonDuplicate(testList)
result2 = solution.singleNonDuplicate(testList2)
print result
print result2
testList = [1, 1, 2, 3, 3, 4, 4, 8, 8]
testList2 = [1, 1, 3, 3, 4, 4, 5, 8, 8]
result = solution.singleNonDuplicate(testList)
result2 = solution.singleNonDuplicate(testList2)
print result
print result2



