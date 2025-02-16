class Solution:
    def isPalindrome(self, s: str) -> bool:
        stripped_s = ""
        for letter in s:
            if letter.isalnum():
                stripped_s = stripped_s + letter.lower()

        return stripped_s == stripped_s[::-1]