class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # left stays, right moves along, uses each letter as a key for its index, if index is greater than left index, letter already in sub
        # string, record distance between left and right, if local max, then move left to right.
        max_lenght = 0
        indicies = {}

        left = 0

        for right in range(len(s)):
            # if current character is already in the map AND last seen index >= left pointer, repeating character is within the current window.
            if s[right] in indicies and indicies[s[right]] >= left:
                left = indicies[s[right]] + 1

            indicies[s[right]] = right

            # window size
            current_length = right - left + 1
            max_lenght = max(max_lenght, current_length)

        return max_lenght

# for debugger
if __name__ == "__main__":
    sol = Solution()

    test_string = "abcabcbb" # test string

    result = sol.lengthOfLongestSubstring(test_string)

    print(result)

    test_string2 = "bbbbb"
    result2 = sol.lengthOfLongestSubstring(test_string2)
    print(result2)

    test_string3 = "pwwkew"
    result3 = sol.lengthOfLongestSubstring(test_string3)
    print(result3)

    test_string4 = ""
    result4 = sol.lengthOfLongestSubstring(test_string4)
    print(result4)

    test_string5 = "a"
    result5 = sol.lengthOfLongestSubstring(test_string5)
    print(result5)