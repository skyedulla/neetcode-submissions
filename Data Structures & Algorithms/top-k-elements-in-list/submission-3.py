class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}
        values = []
        highest_frequency = [[0, 0]]
        for num in nums:
            if num in frequencies:
                frequencies[num] += 1
            else:
                frequencies[num] = 1

            
        #checks every freq of number
        for key, value in frequencies.items():
            
            if value > highest_frequency[-1][0]:
                for i in range(len(highest_frequency)):
                    if value >= highest_frequency[i][0]:
                        highest_frequency.insert(i, [value, key])
                        break

            #if the highest_frequencies list becomes bigger than k, then remove the last pair(this is the lowest frequency)
            if len(highest_frequency) > k:
                highest_frequency.pop()

        list_of_numbers = []
        for pair in highest_frequency:
            list_of_numbers.append(pair[1])

        return list_of_numbers

        
            

        