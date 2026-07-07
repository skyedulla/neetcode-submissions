class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_sequence = 0
        
        for element in nums:
            
            if element - 1 not in num_set:

                i = 1
                sequence_size = 1
                checking = True

                while element + i in num_set:
                    sequence_size += 1
                    i += 1
                    
                max_sequence = max(sequence_size, max_sequence)
        
        return max_sequence
        