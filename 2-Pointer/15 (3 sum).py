from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        answer = []
        nums.sort()

        for x in range(len(nums)):
            if x > 0 and nums[x] == nums[x - 1]:
                continue

            target = -nums[x]
            left = x + 1 
            right = len(nums) - 1

            while left < right:

                current_sum = nums[left] + nums[right]

                if current_sum == target:
                    answer.append([nums[left], nums[right], nums[x]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif current_sum < target:
                    left += 1  # move left pointer right to increase sum

                else:
                    right -= 1  # move right pointer left to decrease sum

        return answer
