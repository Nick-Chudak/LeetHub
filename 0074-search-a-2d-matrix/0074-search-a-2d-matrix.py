class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        h = len(matrix)
        w = len(matrix[0])

        up = 0
        low = h - 1

        while up <= low:
            mid = (up + low) // 2
            
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                l = 0
                r = w - 1
                arr = matrix[mid]
                while l <= r:
                    m = (l + r) // 2
                    if arr[m] < target:
                        l = m + 1
                    elif arr[m] > target:
                        r = m - 1
                    else:
                        return True
                return False

            elif matrix[mid][0] < target:
                up = mid + 1
            else:
                low = mid - 1 
        return False
