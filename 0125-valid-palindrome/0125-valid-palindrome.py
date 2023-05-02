class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            if (s[i].isalpha() or s[i].isnumeric()) == False:
                
                i+= 1
                continue

            if (s[j].isalpha() or s[j].isnumeric())  == False:
                j -= 1
                continue
            
            if s[i].lower() != s[j].lower():
                print(s[i], s[j])
                return False
            i+=1
            j-=1
        return True
                
