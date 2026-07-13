class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = 0
        p2 = 0
        insert_index = 0
        nums1_copy = nums1[:m]

        while p1 < m and p2 < n:
            if nums2[p2] < nums1_copy[p1]:
                nums1[insert_index] = nums2[p2]
                p2 += 1
            
            else:
                nums1[insert_index] = nums1_copy[p1]
                p1 += 1
            
            insert_index += 1
        
        if p1 < m:
            nums1[insert_index:] = nums1_copy[p1:]
        
        if p2 < n:
            nums1[insert_index:] = nums2[p2:]
        
        




        