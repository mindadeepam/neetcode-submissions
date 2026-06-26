
class Solution:
    def trap(self, height: List[int]) -> int:

        total_water = 0
        for i,h in enumerate(height):
            if i==0 or i==(len(height)-1):
                continue
            max_h_on_left = max(height[:i])
            max_h_on_right = max(height[i+1:])
            # print()
            if (max_h_on_right>h) and (max_h_on_left>h):
                water_at_idx = min(max_h_on_left, max_h_on_right)-h
                total_water += water_at_idx
        print(total_water)