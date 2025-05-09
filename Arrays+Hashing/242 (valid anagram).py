class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        dict_s = {}
        dict_t = {}

        for letter in s:
            if (letter in dict_s):
                dict_s[letter] += 1
            else:
                dict_s[letter] = 0
        
        for letter in t:
            if (letter in dict_t):
                dict_t[letter] += 1
            else:
                dict_t[letter] = 0

        if (dict_t == dict_s):
            return True
        else:
            return False
        