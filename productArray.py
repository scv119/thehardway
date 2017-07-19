class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # use O(n) time and O(n) space(list of size n: from_begin, from_end)
        length = len(nums)
        from_begin = []
        from_end = []
        result = []
        result_begin = result_end = 1
        # use fromBegin list to store nums[0] * ... * nums[i]
        # use fromEnd list to store nums[n] * nums[n-1] *... * nums[n - i - 1]
        for i in xrange(0, length):
            result_begin = result_begin * nums[i]
            from_begin.append(result_begin)
            result_end = result_end * nums[length - i - 1]
            from_end.append(result_end)
        for i in xrange(0, length):
            if i == 0:
                result.append(from_end[length - 2])
            elif i == length - 1:
                result.append(from_begin[length - 2])
            else:
                result.append(from_begin[i - 1] * from_end[length - i - 2])
        return result

    def productExceptSelf2(self, nums):
        # use O(n) time and O(1) space if result is not considered as extra space
        length = len(nums)
        begin = end = 1
        result = [1] * length
        for i in xrange(0, length):
            result[i] = result[i] * begin
            begin = begin * nums[i]
            result[length - i -1] = result[length - i - 1] *end
            end = end * nums[length - i -1]
        return result

solution = Solution()
testList = [0, 4, 7, 9, 10]
print solution.productExceptSelf(testList)
print solution.productExceptSelf2(testList)

