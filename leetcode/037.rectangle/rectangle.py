# leetcode: https://leetcode.com/problems/rectangle-area/description/

def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        r1 = abs(A - C) * abs(B - D)
        r2 = abs(E - G) * abs(F - H)
        [A, C] or [C, A] and [E, G] or [G, E]
        [B, D] or [D, B] and [F, H] or [H, F]
        start_x_1 = min(A, C)
        end_x_1 = max(A, C)
        start_y_1 = min(B, D)
        end_y_1 = max(B, D)
        start_x_2 = min(E, G)
        end_x_2 = max(E, G)
        start_y_2 = min(F, H)
        end_y_2 = max(F, H)
        #no overlap area
        if (end_x_2 < start_x_1) or (end_x_1 < start_x_2) or (end_y_2 < start_y_1) or(end_y_1 < start_y_2) :
            return r1 + r2
        overlap_x_start = max(start_x_1, start_x_2)
        overlap_x_end = min(end_x_1, end_x_2)
        overlap_y_start = max(start_y_1, start_y_2)
        overlap_y_end = min(end_y_1, end_y_2)
        overlap_area = abs(overlap_x_start - overlap_x_end) * abs(overlap_y_start - overlap_y_end)
        return r1 + r2 - overlap_area
