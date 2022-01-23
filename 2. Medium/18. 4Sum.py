class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        result = []
        
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                left, right = j + 1, len(nums) - 1
                while left < right:
                    quadraplet = [nums[i], nums[j], nums[left], nums[right]]
                    quadraplet_sum = sum(quadraplet)
                    if quadraplet_sum == target and quadraplet not in result:
                        result.append(quadraplet)
                    elif quadraplet_sum < target:
                        left += 1
                    else:
                        right -= 1
        
        return result

solution = Solution().fourSum([1, 0, -1, 0, -2, 2], 0)
print(solution)