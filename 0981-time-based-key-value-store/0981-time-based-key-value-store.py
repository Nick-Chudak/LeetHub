class TimeMap:

    def __init__(self):
        self.hashkey = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashkey[key] = self.hashkey.get(key, [])
        self.hashkey[key].append([timestamp,value])

    def get(self, key: str, timestamp: int) -> str:
        res = self.hashkey.get(key, None)
        #[hashtable : key -> value] 
        if res == None:
            return ""
        else:

            l = 0
            r = len(res) - 1

            while l <= r:
                mid = (l + r) // 2
                
                if timestamp > res[mid][0]:
                    l = mid + 1
                elif timestamp < res[mid][0]:
                    r = mid - 1
                elif timestamp == res[mid][0]:
                    return res[mid][1]
    
                if l <= r and res[l][0] > timestamp:
                    break
            if res[mid][0] > timestamp:
                return ""
            
        return res[mid][1]

        

        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)