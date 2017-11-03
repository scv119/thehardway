# leetcode: https://leetcode.com/problems/judge-route-circle/description/


def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        move = 0
        direction = {'R': 1, 'L': -1, 'U': 2, 'D':-2}
        for i in moves:
            move += direction[i]
        if move == 0:
            return True
        return False
