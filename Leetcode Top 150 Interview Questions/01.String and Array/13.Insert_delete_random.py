# https://leetcode.com/problems/insert-delete-getrandom-o1/submissions/1318841109/?envType=study-plan-v2&envId=top-interview-150

from random import choice
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict={}
        self.list=[]
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.dict:
            return False
        self.dict[val] =len(self.list)
        self.list.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.dict:
            last_ele = self.list[-1]
            index= self.dict[val]
            self.list[index] =last_ele
            self.dict[last_ele] =index
            
            #delete last ele
            self.list.pop()
            del self.dict[val]
            return True
        
        return False
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return choice(self.list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
