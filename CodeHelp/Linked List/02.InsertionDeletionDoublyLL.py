'''
https://leetcode.com/problems/design-linked-list/solution/
'''
class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None
        self.prev=None
        
class MyLinkedList:

    def __init__(self):
        self.size=0
        self.head=ListNode(0)
        self.tail=ListNode(0)
        self.head.next=self.tail
        self.tail.prev=self.head

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        
        if index+1 < self.size-index:
            curr=self.head
            for _ in range(index+1):
                curr =curr.next
        else:
            curr=self.tail
            for _ in range(self.size-index):
                curr=curr.prev
        return curr.val
    

    def addAtHead(self, val: int) -> None:
        pred=self.head
        succ=self.head.next
        
        self.size=self.size+1
        to_add = ListNode(val)
        to_add.prev=pred
        to_add.next=succ
        
        pred.next=to_add
        succ.prev=to_add

    def addAtTail(self, val: int) -> None:
        succ=self.tail
        pred=self.tail.prev
        
        #same as above
        self.size=self.size+1
        to_add = ListNode(val)
        to_add.prev=pred
        to_add.next=succ
        
        pred.next=to_add
        succ.prev=to_add

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        if index < 0:
            index=0
            
        #find predecessor and successor of the node to be added
        if index < self.size-index:
            pred=self.head
            for _ in range(index):
                pred=pred.next
            succ=pred.next
        else:
            succ=self.tail
            for _ in range(self.size-index):
                succ=succ.prev
            pred=succ.prev
        
        #Insertion itself
        self.size=self.size+1

        to_add = ListNode(val)
        
        to_add.prev=pred
        to_add.next=succ
        
        pred.next=to_add
        succ.prev=to_add
        

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        
        #find predecessor and successor of the node to be added
        if index < self.size-index:
            pred=self.head
            for _ in range(index):
                pred=pred.next
            succ=pred.next.next
        else:
            succ=self.tail
            for _ in range(self.size-index-1):
                succ=succ.prev
            pred=succ.prev.prev
            
        #delete pred.next
        self.size=self.size-1
        pred.next=succ
        succ.prev=pred


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)