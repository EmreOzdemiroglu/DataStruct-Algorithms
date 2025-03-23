from typing import List

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        res = 0
        x1, y1 = points.pop(0)
        while points:
            x2, y2 = points.pop(0)
            res += max(abs(x2-x1), abs(y2-y1))
            x1, y1 = x2, y2
        return res
