'''
https://leetcode.com/problems/design-hashmap/submissions/
'''
class MyHashMap:

    def __init__(self):
        self.bucket =[]

    def put(self, key: int, value: int) -> None:
        found=False
        for i,kv in enumerate(self.bucket):
            if key == kv[0]:
                self.bucket[i] =(key,value)
                found=True
                break
        if not found:
            self.bucket.append((key,value))


    def get(self, key: int) -> int:
        for (k,v) in self.bucket:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        for i,kv in enumerate(self.bucket):
            if key == kv[0]:
                del self.bucket[i]


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)