class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        for i in range(1, len(height) - 1):
            maxLeft = max(height[:i]) #max height to the left of i
            maxRight = max(height[i + 1:]) #max height to the right of i
            addition = min(maxLeft, maxRight) - height[i]
            if addition > 0:
                res += addition
        return res


