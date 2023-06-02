class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        res = nums[0]
        while l <= r:
            print("executed")
            mid = (l + r) // 2
            if nums[r] >= nums[l]:
                res = min(res, nums[l])
                return res
            
            if nums[mid] >= nums[l]:
                print("executed")
                print(mid)
                l = mid + 1
                res = min(res, nums[mid])
            else:
                print("else - ", mid)
                r = mid - 1
                res = min(res, nums[mid])

        return res

