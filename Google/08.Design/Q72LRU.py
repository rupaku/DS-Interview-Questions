'''
https://leetcode.com/problems/lru-cache/submissions/
https://www.youtube.com/watch?v=kGlSZdDfm8M

get from dict and add to end
put to end of dictionary
'''
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache=[]
        self.map ={}
            
    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        self.cache.remove(key)
        self.cache.append(key)
        return self.map[key]
        

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.cache.remove(key)
            self.cache.append(key)
            self.map[key]=value
            return None
        if self.capacity <= len(self.map):
            k=self.cache.pop(0)
            self.map.pop(k)
            self.map[key]=value
        else:
            self.map[key]=value
        self.cache.append(key)
        return None
           


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)