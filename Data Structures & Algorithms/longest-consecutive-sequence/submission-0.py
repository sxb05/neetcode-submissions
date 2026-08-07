class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        output = 1
        for n in range(1, len(nums)):
            if nums[n] - nums[n-1] == 1:
                output += 1
        return output

        