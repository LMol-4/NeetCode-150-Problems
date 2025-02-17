class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        """answer = []
        calculations = {}

        for i in range(len(numbers)):
            if (target-numbers[i]) in calculations:
                answer.append(calculations[target-numbers[i]]+1)
                answer.append(i+1)
                return answer
            calculations[numbers[i]] = i"""

        left = 0
        right = len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]

            if current_sum == target:
                return [left + 1, right + 1]

            elif current_sum < target:
                left += 1  # move left pointer right to increase sum

            else:
                right -= 1  # move right pointer left to decrease sum