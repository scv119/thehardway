# leetcode: https://leetcode.com/problems/maximum-product-subarray/description/

def maxProduct(self, nums):
    # time complexity: O(n^2), space complexity O(n)
    result = [nums[0]]
    for i in xrange(1, len(nums)):
        j = i - 1
        temp = nums[i]
        max_product = temp
        while j >= 0:
            temp = temp * nums[j]
            if temp > max_product:
                max_product = temp
            j = j - 1
        result.append(max(result[i-1], max_product))
    return result[len(nums) - 1]

def maxProduct(self, nums):
    # time complexity: O(n). space: O(1)
    cur_max = nums[0];
    temp_max = temp_min = cur_max
    for i in xrange(1, len(nums)):
        if nums[i] < 0:
            temp_max, temp_min = temp_min, temp_max
        temp_max = max(nums[i], temp_max*nums[i])
        temp_min = min(nums[i], temp_min*nums[i])
        cur_max = max(cur_max, temp_max)
    return prev


