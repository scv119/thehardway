# leetcode: https://leetcode.com/problems/partition-equal-subset-sum/description/

def canPartition(self, nums):
    # space complexity: O(n), n is the half of sum, time complexity: O(n^2)
    total_sum = sum(nums)
    if total_sum % 2 != 0:
        return False
    half = total_sum / 2
    reachability = [False for i in xrange(half + 1)]
    reachability[0] = True
    for num in nums:
        for i in xrange(half, num - 1, -1):
            if reachability[i - num] == True:
                reachability[i] = True
    return reachability[half]
