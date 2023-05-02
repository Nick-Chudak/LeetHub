class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        longest = 0
        for i in range(len(nums)):
            if (nums[i] - 1) not in hashset:
                curr = 0
                while nums[i] + curr in hashset:
                    curr +=1
                longest = max(curr, longest)
        return longest
        
            