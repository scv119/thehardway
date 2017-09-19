# leetcode: https://leetcode.com/problems/sqrtx/description/

def mySqrt(self, x):
    # time: O(lgn), space: O(1)
    l = 0
    r = x
    while l <= r:
        m = (l + r) /2
        if l * l == x or (l * l < x and (l + 1) * (l + 1) > x):
            return 1
        if r * r == x:
            return r
        if m * m == x:
            return m
        elif m * m > x:
            r = m
        elif m * m < x:
            l = m
