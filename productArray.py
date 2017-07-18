class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #use O(n) time and O(n) space
        length = len(nums)
        fromBegin = []
        fromEnd = []
        result = []
        resultB = resultE = 1
        #use fromBegin list to store nums[0] * ... * nums[i]
        #use fromEnd list to store nums[n] * nums[n-1] *... * nums[n - i - 1]
        for i in range(0, length):
            resultB = resultB * nums[i]
            fromBegin.append(resultB)
            resultE = resultE * nums[length - i - 1]
            fromEnd.append(resultE)
        for i in range(0, length):
            if i == 0:
                result.append(fromEnd[length - 2])
            elif i == length - 1:
                result.append(fromBegin[length - 2])
            else:
                result.append(fromBegin[i-1] * fromEnd[length - i -2])
        return result

    def productExceptSelf2(self, nums):
        length = len(nums)
        begin = end = 1
        result = [1] * length
        for i in range(0, length):
            result[i] = result[i] * begin
            begin = begin * nums[i]
            result[length - i -1] = result[length - i - 1] *end
            end = end * nums[length - i -1]
        return result

a =Solution()
testList = [0, 4, 7, 9, 10]
print a.productExceptSelf(testList)
print a.productExceptSelf2(testList)

