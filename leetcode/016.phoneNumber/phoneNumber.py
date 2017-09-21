# leetcode: https://leetcode.com/problems/letter-combinations-of-a-phone-number/#/description

class Solution(object):
    def letterCombination(self, digits):
        """
        : type digits: str
        : rtype: List[str]
        """
        length = len(digits)
        table = [[" "], ["*"], ["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"], ["j", "k", "l"], ["m", "n", "0"], ["p", "q", "r", "s"], ["t", "u", "v"], ["w", "x", "y", "z"]]
        result = []
        for digit in digits:
            num = int(digit)
            temp = []
            for i in table[num]:
                temp = temp + self.helper(result, i)
            result = temp
        return result

    def helper(self, prev_list, single_char):
        if prev_list == []:
            prev_list = [single_char]
        else:
            temp = []
            for i in prev_list:
                temp.append(i + single_char)
            prev_list = temp
        return prev_list

solution = Solution()
test_str = "0123"
print solution.letterCombination(test_str)
