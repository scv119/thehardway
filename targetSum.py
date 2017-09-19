# leetcode: https://leetcode.com/problems/target-sum/description/

def findTargetSumWays(self, nums, S):
    # time: O(ns), space O(ns)
    if nums == []:
        return 0
    if nums[0] != 0:
        dic = {nums[0]:1, - nums[0]:1}
    else:
        dic = {0:2}
    for i in xrange(1, len(nums), 1):
        tdic = {}
        for d in dic:
            tdic[d + nums[i]] = tdic.get(d + nums[i], 0) + dic.get(d, 0)
            tdic[d - nums[i]] = tdic.get(d - nums[i], 0) + dic.get(d, 0)
        dic = tdic
    return dic.get(S, 0)
