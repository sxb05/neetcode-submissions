class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
    
    # If the array is not rotated (or has 1 element)
        if nums[low] <= nums[high]:
            return nums[low]
            
        while low < high:
            mid = low + (high - low) // 2
            
            # If mid element is greater than the highest element, 
            # the minimum must be in the right half.
            if nums[mid] > nums[high]:
                low = mid + 1
            # Otherwise, the minimum is in the left half (including mid).
            else:
                high = mid
                
        return nums[low]