class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        closest, closest_sum = 999999, 9999999
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if abs(nums[i] + nums[j] + nums[k] - target) < closest_sum:
                        closest = nums[i] + nums[j] + nums[k]
                        closest_sum = abs(nums[i] + nums[j] + nums[k] - target)
        
        return closest


solution = Solution().threeSumClosest([-1, 2, 1, -4], 1)
print(solution)