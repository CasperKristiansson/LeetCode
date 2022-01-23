class Solution:
    def maxAreaForce(self, height: List[int]) -> int:
        result = 0
        for i in range(len(height)):
            for j in range(i, len(height)):
                result = max(result, min(height[i], height[j]) * (j - i))
        
        return result

    def maxArea(self, height: List[int]) -> int:
        left, right, result = 0, len(height) - 1, 0
        while left < right:
        	result = max((right - left) * min(height[left],height[right]), result)
        	if height[left] < height[right]:
        		left += 1
        	else:
        		right -= 1
        
        return result