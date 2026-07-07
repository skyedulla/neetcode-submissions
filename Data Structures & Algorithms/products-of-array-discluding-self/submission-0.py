class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        number_of_zeros = 0
        for num in nums:
            if num == 0:
                number_of_zeros += 1
            else:
                product *= num


        answer = []
        
        for i in range(len(nums)):

            if number_of_zeros >= 2:
                answer.append(0)


            elif number_of_zeros == 1:

                if nums[i] == 0:
                    answer.append(product)
                else:
                    answer.append(0)


            else:
                answer.append(int(product / nums[i]))
        
        return answer

                

            
