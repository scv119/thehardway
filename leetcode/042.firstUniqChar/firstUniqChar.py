# leetcode: https://leetcode.com/problems/first-unique-character-in-a-string/description/


def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = {}
        char_list = list(s)
        for i in char_list:
            if i not in res:
                res[i] = 1
            else:
                res[i] += 1
        for i in xrange(len(char_list)):
            if res[char_list[i]] == 1:
                return i
        return -1
