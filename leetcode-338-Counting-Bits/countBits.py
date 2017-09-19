# leetcode: https://leetcode.com/problems/counting-bits/#/description

class Solution(object):
    def countBits(self, num):
        """
        : type num: int
        : rtype: List[int]
        """
        # requirement: time complexity O(n), space complexity O(n)
        # first though is to use DP, use result list to memoize previous result
        # find the rule: f(i) = f(i - Top) + 1
        # top here means i > 2^n, max(2^n)
        i = 1
        result = [0]
        temp_result = 0
        temp_top = 1
        while i <= num:
            if i == temp_top:
                result.append(1)
                temp_top = 2 * temp_top
            else:
                temp_result = result[i - temp_top / 2] + 1
                result.append(temp_result)
            i = i + 1
        return result

solution = Solution()
num = 23
print solution.countBits(num)
