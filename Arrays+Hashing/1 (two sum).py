class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """answer = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    if nums[i] + nums[j] == target:
                        answer.append(i)
                        answer.append(j)
                        return answer"""
        
        answer = []
        calculations = {}

        for i in range(len(nums)):
            if (target-nums[i]) in calculations:
                answer.append(i)
                answer.append(calculations[target-nums[i]])
            calculations[nums[i]] = i
        
        return answer