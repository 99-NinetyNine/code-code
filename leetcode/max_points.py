"
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.
Algortihms:
  for each point i, we need to compute the slopes.
  For each another point j , j!=i we compute slope as rational number e.g.(2,1) which acts as key to slopes. However if point_i == point_j they are in same line so we update the same point count.

  After each point is checked, a max of previous count, sum of max of slopes.values() if slopes else same point count and (1 for point i) is computed.
  
 In this way max_points_on_line is updated for each point. Eventually accounting for the solution.

Nice Trick: We use defaultdict and saved the slope in terms of rational number computed by dividing with the gcd ensuring z= p/q, p, q E I. I is set of Integers.
  


"
from math import gcd
from functools import reduce
from collections import defaultdict

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:

        if len(points) < 2:
            return len(points)
        
        max_points_on_line = 1
        
        for i in range(len(points)):
            slopes = defaultdict(int)
            same_point_count = 0
            for j in range(len(points)):
                if i != j:
                    if points[i] == points[j]:
                        same_point_count += 1
                    else:
                        dx = points[j][0] - points[i][0]
                        dy = points[j][1] - points[i][1]
                        
                        # Reduce slope to its simplest form using gcd
                        if dx == 0:  # Vertical line case
                            slope = (float('inf'), points[i][0])
                        else:
                            g = gcd(dx, dy)
                            dx //= g
                            dy //= g
                            slope = (dy, dx)
                        
                        slopes[slope] += 1
            
            if slopes:
                max_points_on_line = max(max_points_on_line, max(slopes.values()) + same_point_count + 1)
            else:
                max_points_on_line = max(max_points_on_line, same_point_count + 1)
        
        return max_points_on_line
