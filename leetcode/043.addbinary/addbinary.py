# leetcode: https://leetcode.com/problems/add-binary/description/

def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a_list = list(a)
        b_list = list(b)
        res = ""
        carry = 0
        while len(a_list) > 0 or len(b_list) > 0:
            if len(a_list) > 0 and len(b_list) > 0:
                cur_a = a_list.pop()
                cur_b = b_list.pop()
                if cur_a == cur_b == "1":
                    if carry == 0:
                        res = "0" + res
                    else:
                        res = "1" + res
                    carry = 1
                elif cur_a == cur_b == "0":
                    if carry == 0:
                        res = "0" + res
                    else:
                        res = "1" + res
                    carry = 0
                else:
                    if carry == 0:
                        carry = 0
                        res = "1" + res
                    else:
                        carry = 1
                        res = "0" + res
            elif len(a_list) > 0:
                cur_a = a_list.pop()
                if cur_a == "1":
                    if carry == 0:
                        res = "1" + res
                        carry = 0
                    else:
                        res = "0" + res
                        carry = 1
                else:
                    if carry == 0:
                        res = "0" + res
                    else:
                        res = "1" + res
                    carry = 0
            elif len(b_list) > 0:
                cur_b = b_list.pop()
                if cur_b == "1":
                    if carry == 0:
                        res = "1" + res
                    else:
                        res = "0" + res
                        carry = 1
                else:
                    if carry == 0:
                        res = "0" + res
                    else:
                        res = "1" + res
                    carry = 0
        if carry == 1:
            res = "1" + res
        return res

def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a_list = list(a)
        b_list = list(b)
        carry = 0
        res = ""
        while len(a_list) > 0 or len(b_list) > 0:
            if len(a_list) == 0:
                cur_a = 0
            else:
                cur_a = int(a_list.pop())
            if len(b_list) == 0:
                cur_b = 0
            else:
                cur_b = int(b_list.pop())
            sum_value = cur_a + cur_b
            if carry == 1:
                sum_value += 1
            if sum_value >= 2:
                carry = 1
            else:
                carry = 0
            res = str(sum_value % 2) + res
        if carry == 1:
            res = "1" + res
        return res
