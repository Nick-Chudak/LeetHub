class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        arr = range(1, max(piles) + 1)
        l = 0
        r = len(arr)
        res = r
        while l <= r:
            mid = (l + r) // 2 # mid is index of k what we're trying
            k = arr[mid]

            time = 0
            for i in range(len(piles)):
                time += (piles[i] // k) + 1 if piles[i] % k != 0 else (piles[i] // k)
            #binary search options
            if time <= h:
                r = mid - 1
                res = min(res,k)
            if time > h:
                l = mid + 1

        return res

