'''
https://leetcode.com/problems/time-based-key-value-store/submissions/
'''
class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.timestamp_map={}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timestamp_map:
            self.timestamp_map[key]=[]
        self.timestamp_map[key].append((timestamp,value))
     
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timestamp_map:
            return ""
        for i in range(len(self.timestamp_map[key])-1,-1,-1):
            ele=self.timestamp_map[key][i]
            time=ele[0]
            if time <= timestamp:
                return ele[1]
            
        return ""
                


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)