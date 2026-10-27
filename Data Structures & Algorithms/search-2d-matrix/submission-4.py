class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for l in matrix:

            
            if l[-1] >= target:

                left = 0
                right = len(l) - 1

                
                while left <= right:

                    mid = (left + right) // 2

                    if l[mid] == target:
                        return True

                    elif l[mid] > target:
                        right = mid - 1

                    else:
                        left = mid + 1

                return False

        return False

        