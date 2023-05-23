class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0

        slow = 0
    
        hashset = set()
        maxSubstring = 0
        for fast in range(len(s)):
            while s[fast] in hashset:
                hashset.remove(s[slow])
                slow +=1
            hashset.add(s[fast])
            maxSubstring = max(fast - slow + 1, maxSubstring)

        return maxSubstring
        
            





