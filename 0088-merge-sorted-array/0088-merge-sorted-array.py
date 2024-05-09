class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1  # Last index of the initial part of nums1 that contains values
        k = m + n - 1  # Last index of nums1
        j = n - 1  # Last index of nums2

        while j >= 0:
            # Check if all elements from nums1 have been merged
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1  # Move the end pointer in nums1 to the left after placing an element



            
                
                
                
                
                
                 
                

    
        