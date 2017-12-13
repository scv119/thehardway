# leetcode: https://leetcode.com/problems/rotate-array/description/

 def rotate(self, nums, k):
        k = k % len(nums)
        self.reverse(nums, 0, len(nums) - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, len(nums) - 1)

    def reverse(self, nums, start, end):
        while start < end:
            temp = nums[start]
            nums[start] = nums[end]
            nums[end] = temp
            start += 1
            end -= 1

def rotate(self, nums, k):
    new_list = nums[:]
    for i in xrange(len(nums)):
        index = (i + k) % len(nums)
        new_list[index] = nums[i]
    nums = new_list

def rotate(self, nums, k):
    start = 0
    j = (start + k) % len(nums)
    tempValue = nums[start]
    counter = 0
    while counter < len(nums):
        # a cycle ends
        if j == start:
            nums[start] = tempValue
            counter += 1
            if counter >= len(nums):
                break
            start += 1
            j = (start + k) % len(nums)
            tempVaue = nums[start]
        temp = nums[j]
        nums[j] = tempValue
        tempValue = temp
        j = (j + k) % len(nums)
        counter += 1
    
