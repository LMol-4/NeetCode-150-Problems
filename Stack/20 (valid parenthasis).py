class Solution:
    def isValid(self, s: str) -> bool:
        """right = ['}', ']', ')']
        stack = []

        for index in range(len(s)):
            if s[index] in right and stack:
                ans = stack.pop()
                if (ord(s[index]) - ord(ans)) not in [1,2]:
                    return False
            else:
                stack.append(s[index])
        
        if not stack:
            return True
        else:
            return False"""
        
        stack = []
        bracketPairs = { ")" : "(", "]" : "[", "}" : "{" }

        for bracket in s:
            if bracket in bracketPairs:
                if stack and stack[-1] == bracketPairs[bracket]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracket)
        
        if not stack:
            return True
        else:
            return False