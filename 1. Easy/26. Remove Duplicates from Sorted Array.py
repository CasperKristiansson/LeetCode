class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:        
        i, j = 0, 0
        
        while i < len(nums):
            j = i + 1
            while j < len(nums) and nums[j] == nums[i]:
                del nums[j]
            i += 1
    
        return len(nums)

solution = Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4])
print(solution)