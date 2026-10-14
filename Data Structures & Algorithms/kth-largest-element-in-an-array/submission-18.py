class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # l = len(nums)
        # res = 0
        # nums = [-n for n in nums]
        
        # heapq.heapify(nums)
        
        # for _ in range(k):

        #     res = heapq.heappop(nums)

        # if res < 0:
        #     res = abs(res) 
        # return res

        return heapq.nlargest(k, nums)[-1]

        