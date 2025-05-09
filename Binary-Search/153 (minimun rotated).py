class Solution:
    def findMin(self, nums: List[int]) -> int:
        # two groups left and right of midpoint
        left = 0
        right = len(nums) - 1
        current_smallest = nums[0]

        while left <= right:
            # full loop condition
            if nums[left] < nums[right]:
                current_smallest = min(current_smallest, numbers[left])
                break
            
            mid = (right + left) // 2

            current_smallest = min(current_smallest, numbers[mid])

            # in right
            if nums[mid] >= nums[left]:
                left = mid + 1
            # in left
            else:
                right = mid - 1
        
        return current_smallest
    
"""sol = Solution()
numbers = [4,5,6,7,0,1,2]
smallest = sol.findMin(numbers)
print(smallest)"""