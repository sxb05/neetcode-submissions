from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        if not nums or k == 0:
            return []
            
        result = []
        q = deque()  # Stores indices of elements
        
        for i in range(len(nums)):
            # 1. Remove indices that are out of the current window bounds
            if q and q[0] < i - k + 1:
                q.popleft()
                
            # 2. Maintain decreasing order: remove smaller elements from the back
            while q and nums[q[-1]] < nums[i]:
                q.pop()
                
            # 3. Add the current element's index
            q.append(i)
            
            # 4. Once the first window is fully formed, append the max to the result
            if i >= k - 1:
                result.append(nums[q[0]])
                
        return result

            