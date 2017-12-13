# leetcode: https://leetcode.com/problems/zigzag-conversion/description/

def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        interval = 2 * numRows - 2
        res = ['' for i in xrange(numRows)]
        for i in xrange(len(s)):
            if i % interval < numRows:
                index = i % interval
            else:
                index = interval - i % interval
            res[index] += s[i]
        resStr=""
        for i in res:
            resStr += i
        return resStr
