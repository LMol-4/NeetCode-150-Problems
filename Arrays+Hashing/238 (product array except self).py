class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #brute force
        """ans = []
        for i in range(len(nums)):
            current = 1
            for j in range(len(nums)):
                if i != j:
                    current = current * nums[j]
            
            ans.append(current)
        
        return ans"""
        
        #Prefix - suffix (slow)

        """ans = []
        prefix = []
        suffix = []
        prefix_num = 1
        suffix_num = 1
        for i in range(len(nums)-1):
            prefix_num = nums[i] * prefix_num
            prefix.append(prefix_num)

            suffix_num = nums[len(nums)-1-i] * suffix_num
            suffix.append(suffix_num)
        
        ans.append(suffix.pop())

        for i in range(len(prefix)):
            if i < len(prefix)-1:
                ans.append(prefix[i]*suffix[-1-i])
            else:
                ans.append(prefix[i])
        
        return ans"""

        # Prefix - suffix (efficient memory)

        answer = [1]*len(nums)
        prefix = 1
        postfix = 1
        
        for i in range(len(nums)):
            answer[i] = prefix
            prefix *= nums[i]

        for i in range(len(nums) - 1, -1, -1):
            answer[i] *= postfix
            postfix *= nums[i]

        return answer