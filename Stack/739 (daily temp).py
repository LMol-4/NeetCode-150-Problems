class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Input: temperatures = [73,74,75,71,69,72,76,73]
        Output: [1,1,4,2,1,1,0,0]
        """

        # [1,1,0,2,1,0,0,0]
        # [75, 71,]

        ans = [0] * len(temperatures)
        stack = []

        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:

                stackTemp, stackIndex = stack.pop()
                ans[stackIndex] = (index - stackIndex)
            
            stack.append([temp,index])

        return ans