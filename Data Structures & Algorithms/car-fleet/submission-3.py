class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        #If I convert pos and speed into a time array

        #I will iterate

        for i in range(len(position)):
            time = (target - position[i]) / speed[i]

            position[i] = (position[i], time)
        
        data = position

        data.sort(key=lambda item: -item[0])

        fleets = 1
        time_required = data[0][1]
        for i in range(1, len(data)):
            time = data[i][1]
            if time > time_required:
                time_required = time
                fleets += 1
        
        return fleets

                





    


        
        
