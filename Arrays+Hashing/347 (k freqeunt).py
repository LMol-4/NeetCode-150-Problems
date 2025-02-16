class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}

        for number in nums:
            frequency[number] = 1 + frequency.get(number, 0)
            
        rank = [key for key, _ in sorted(frequency.items(), key=lambda item: item[1], reverse=True)[:k]]

        return rank

        """rank = [[] for _ in range(len(nums) + 1)]

        for number, count in frequency.items():
            rank[count].append(number)

        answer = []

        for i in range(len(rank) - 1, 0, -1):

            for number in rank[i]:
                answer.append(number)

                if len(answer) == k:
                    return answer"""