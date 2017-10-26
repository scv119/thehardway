# leetcode: https://leetcode.com/problems/decode-string/description/

def decodeString(self, s):
    """
    :type s: str
    :rtype: str
    """
    stack = []
    i = 0
    num = 0
    for i in xrange(len(s)):
        # a-z
        if (ord(s[i]) >= 97 and ord(s[i]) <= 122):
            stack.append(s[i])
        # [
        elif s[i] == "[":
            stack.append(num)
            num = 0
            i = i + 1
        # ]
        elif s[i] == "]":
            char = stack.pop()
            temp = ""
            while type(char) != int:
                temp = char + temp
                char = stack.pop()
            temp = char * temp
            stack.append(temp)
            i = i + 1
        # int
        else:
            num = 10 * num + int(s[i])
    res = ""
    while stack != []:
        res = stack.pop() + res
    return res
