class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if not (len(s1) > len(s2)):
            lettercount = [0] * 26
            runningcount = [0] * 26
            windowsize = len(s1)
            left = 0
            right = 0

            for letter in s1:
                letterindex = ord(letter) - 97
                lettercount[letterindex] += 1

            while right != len(s2):
                letterindex = ord(s2[right]) - 97
                runningcount[letterindex] += 1
                if (right - left) == windowsize:
                    letterindex = ord(s2[left]) - 97
                    runningcount[letterindex] -= 1
                    left += 1
                
                if lettercount == runningcount:
                    return True

                right += 1

        return False

"""sol = Solution()
s1 = "ab"
s2 = "eidbaooo"
print(sol.checkInclusion(s1,s2))

stringtest = 'd'

print(ord(stringtest)-97)"""