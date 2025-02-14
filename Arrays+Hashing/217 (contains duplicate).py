class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        number_list = {}

        for number in nums:
            if (number in number_list):
                return True
            else:
                number_list[number] = number
            
        return False
