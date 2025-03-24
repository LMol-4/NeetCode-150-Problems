class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #slow
        """
        ans = 0
        prev_numbers = {}
        for number in nums:
            prev_numbers[number] = True
            i = 1
            j = 1
            total = 1
            while number-i in prev_numbers.keys():
                i += 1
                total += 1

            while number+j in prev_numbers.keys():
                j += 1
                total += 1
            
            if total > ans:
                ans = total

        return ans
        """

        #hash set
        number_set = set(nums)
        ans = 0

        for num in number_set:
            if (num - 1) not in number_set: # must be start of sequence, no smaller
                length = 1
                while (num + length) in number_set:
                    length += 1
                ans = max(length, ans)
                
        return ans