class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def eatingSimulation(rate):
            hours = 0
            for bananas in piles:
                hours += int(math.ceil(bananas / rate))

            if hours <= h:
                return True
            else:
                return False

        low = 1 
        high = max(piles) 
        
        while low < high:
            mid = (low + high) // 2
            if eatingSimulation(mid) == False:
                low = mid + 1
            else:
                high = mid

        return high
        
        # low = 34 and high = 36, then mid becomes 35 if its false low = high
        
        
        #low = 34 and high = 35




        
