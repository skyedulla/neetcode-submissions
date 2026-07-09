class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        L = 0
        R = len(arr) - 1

        while R - L > k - 1:
            if abs(arr[R] - x) < abs(arr[L] - x):
                L += 1

            elif abs(arr[R] - x) > abs(arr[L] - x):
                R -= 1

            else:
                if abs(arr[L + 1] - x) < abs(arr[R - 1] - x):
                    L += 1
                else:
                    R -= 1

        array = []
        for i in range(L, R + 1):
            array.append(arr[i])
        
        return array




                
                