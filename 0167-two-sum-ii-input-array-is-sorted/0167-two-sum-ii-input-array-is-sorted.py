class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Iterate over each element of the array, on each iteration create a hasmap. Key = element, value = index of the element. On each iteration substract current value from the target. And check whether the difference is in the hashmap. If it's in the hashmap -> return index <- won't work. Only constant space"""
        """
        Start iteration from the left and right. Compare current sum (left pointer + right pointer) against the target value. If current value > target -> decrease right pointer, if current value < target -> increase left pointer."""
        i = 0
        j = len(numbers) - 1
        while i < j:
            curr_sum = numbers[i] + numbers[j]
            if curr_sum > target:
                j-=1
                continue
            if curr_sum < target:
                i+=1 
                continue
            return [i + 1, j + 1]