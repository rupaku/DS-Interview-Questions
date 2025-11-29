class Node:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None

    # --------------------------
    # INSERTION OPERATIONS
    # --------------------------

    def insert_at_head(self, val:int) -> Node:
        new_node = Node(val ,self.head)
        self.head = new_node

    def insert_at_tail(self, val):
        new_node = Node(val)
        if not self.head:
            self.head=new_node
            return
        
        curr=self.head
        while curr.next:
            curr=curr.next
        curr.next=new_node

    def insert_at_position(self,val,pos):
        new_node=Node(val)

        if pos == 0:
            self.insert_at_head()
            return 
        curr=self.head
        for _ in range(pos-1):
            if not curr:
                return #out of range
            curr=curr.next

        new_node.next=curr.next
        curr.next=new_node

    # --------------------------
    # DELETION OPERATIONS
    # --------------------------

    def delete_at_head(self):
        if not self.head:
            return
        self.head=self.head.next

    def delete_at_tail(self):
        if not self.head:
            return
        if not self.head.next:
            self.head=None
            return

        curr=self.head
        while curr.next and curr.next.next:
            curr=curr.next

        curr.next = None

    def delete_at_position(self,pos):
        if not self.head:
            return
        if pos==0:
            self.delete_at_head()
            return
        curr=self.head
        for _ in range(pos-1):
            if not curr.next:
                return
            curr=curr.next

        if curr.next:
            curr.next=curr.next.next

    def delete_value(self, target):
        """Delete first occurrence of value."""
        if not self.head:
            return
        
        if self.head.val == target:
            self.delete_at_head()
            return
        
        curr=self.head
        while curr.next:
            if curr.next.val == target:
                curr.next=curr.next.next
                return
            curr=curr.next

    # --------------------------
    # PRINT OPERATION
    # --------------------------
    def print_list(self):
        curr = self.head
        while curr.next:
            print(curr.val,end="->")
            curr= curr.next
        print("None")



if __name__ == "__main__":
    ll= LinkedList()
    ll.insert_at_head(3)
    ll.insert_at_head(2)
    ll.insert_at_head(1)

    ll.insert_at_tail(4)
    ll.insert_at_tail(5)

    ll.insert_at_position(99, 3)

    ll.delete_at_head()

    ll.delete_at_tail()

    ll.delete_at_position(2)

    ll.delete_value(3)

    ll.print_list()
