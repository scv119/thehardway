# leetcode : https://leetcode.com/problems/reverse-words-in-a-string-ii/description/

def reverseWords(self, str):
        """
        :type str: List[str]
        :rtype: void Do not return anything, modify str in-place instead.
        """
        self.reverseList(str, 0, len(str) - 1)
        start = 0
        for i in xrange(len(str)):
            if str[i] == ' ':
                self.reverseList(str, start, i-1)
                start = i + 1
        self.reverseList(str, start, len(str)-1)

    def reverseList(self, str, start, end):
        while start < end:
            temp = str[start]
            str[start] = str[end]
            str[end] = temp
            start += 1
            end -= 1
