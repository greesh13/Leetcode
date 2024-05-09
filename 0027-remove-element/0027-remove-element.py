class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        pop_count = 0
    # Iterate over the list backwards
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == val:
                nums.pop(i)
                pop_count += 1

        
