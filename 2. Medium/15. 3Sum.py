class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []
        hashmap = {nums[i]: i for i in range(len(nums))}

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                complement = - nums[i] - nums[j]
                
                if complement in hashmap and hashmap[complement] != i and hashmap[complement] != j:
                    result.append([nums[i], nums[j], complement])

        non_duplicate_result = []

        for i in result:
            i = sorted(i)
            if i not in non_duplicate_result:
                non_duplicate_result.append(i)

        return non_duplicate_result

solution = Solution().threeSum([-1, 0, 1, 2, -1, -4])
print(solution)