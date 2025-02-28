import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #bruteforce 
        """speed = 1
        while True:
            total_time = 0
            for pile in piles:
                total_time += math.ceil(pile / speed)
            
            if total_time <= h:
                return speed
            speed += 1"""
        
        #binary search
        lowerbound = 1
        upperbound = max(piles)
        answer = upperbound

        while lowerbound <= upperbound:
            total_time = 0
            speed = lowerbound + ((upperbound - lowerbound) // 2)

            for pile in piles:
                total_time += math.ceil(pile / speed)
            
            if (total_time <= h): # decrese speed of eating.
                answer = min(answer, speed)
                upperbound = speed - 1

            elif (total_time > h): # increase speed of eating
                lowerbound = speed + 1
        
        return answer