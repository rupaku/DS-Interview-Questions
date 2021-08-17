'''
https://leetcode.com/problems/snapshot-array/submissions/
'''
class SnapshotArray(object):

    def __init__(self, length):

        self.id = -1
        self.items = []
        self.dict_map = {}

    def set(self, index, val):

        self.dict_map[index] = val
        
    def snap(self):

        self.items.append(self.dict_map)
        self.dict_map = self.dict_map.copy()
        self.id += 1
        return self.id 
        
    def get(self, index, snap_id):

        try:
            d = self.items[snap_id]
            return d[index]
        except KeyError:
            return 0
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)