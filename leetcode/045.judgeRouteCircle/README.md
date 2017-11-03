https://leetcode.com/problems/judge-route-circle/description/

1, method: count how many R in string, how many L in string, how many U in string and how many D in string. R = L, U = D.
   space complexity: O(1), time complexity: O(n)

2, at first, I used -1 represent R, 1 represent L, 2 represents U, -2 represents D. Check the sum of moves. But it does not work because it may have string like "RRU"
