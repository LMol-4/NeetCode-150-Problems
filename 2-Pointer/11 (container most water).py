class Solution:
    def maxArea(self, height: List[int]) -> int:
        """max_area = 0
        for i in range(len(height)):
            for j in range(len(height)):
                if height[i] > height[j]:
                    current_area = height[j] * (j - i)
                else:
                    current_area = height[i] * (j - i)
                
                if current_area > max_area:
                    max_area = current_area
        
        return max_area"""
        left = 0
        right = len(height) - 1
        max_area = 0

        while left != right:
            if height[left] > height[right]:
                current_area = height[right] * (right - left)
            else:
                current_area = height[left] * (right - left)
            
            if max_area < current_area:
                max_area = current_area

            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        
        return max_area