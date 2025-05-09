class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            # (left + right) // 2 can lead to overflow
            m = left + ((right - left) // 2)  

            if nums[m] > target:
                right = m - 1

            elif nums[m] < target:
                left = m + 1
                
            else:
                return m
            
        return -1