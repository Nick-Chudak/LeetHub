class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            value = hashmap.get(target - nums[i], None)
            hashmap[nums[i]] = i
            if value != None:
                return [i,value]
        
        