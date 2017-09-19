# leetcode: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

def twoSum(self, numbers, target):
    """
    : numbers: List[int], sorted
    : target: int
    : rtype: List[int]
    """
    # time: O(n), space: O(1)
    i = 0
    j - len(numbers) - 1
    while i < j:
        if numbers[i] + numbers[j] == target:
            return [i+1, j+1]
        elif numbers[i] + numbers[j] > target:
            j = j - 1
        elif numbers[i] + numbers[j] < target:
            i = i + 1

