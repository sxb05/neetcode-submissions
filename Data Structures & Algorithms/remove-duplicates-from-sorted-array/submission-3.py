class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0

        for r in range(1, len(nums)):
            if nums[r] != nums[left]:
                left += 1
                nums[left] = nums[r]

        return left + 1
        