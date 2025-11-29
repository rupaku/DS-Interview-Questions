class Node:
    def __init__(self,val=0):
        self.val=val
        self.next=None
        self.prev=None

class DoublyLL:
    def __init__(self):
        self.head=None

    # ----------------------------
    # INSERTIONS
    # ----------------------------

    def insert_at_head(self,val):
        new_node=Node(val)
        new_node.next = self.head

        if self.head:
            self.head.prev = new_node

        self.head = new_node

    def insert_at_tail(self, val: int):
        new_node = Node(val)

        if not self.head:
            self.head = new_node
            return

        curr = self.head
        while curr.next:
            curr = curr.next

        curr.next = new_node
        new_node.prev = curr

    def insert_at_position(self, val, pos):
        new_node = Node(val)

        if pos == 0:
            self.insert_at_head()
            return
        
        curr=self.head
        for _ in range(pos-1):
            if not curr:
                return
            curr=curr.next

        new_node.next = curr.next
        new_node.prev = curr

        if curr.next:
            curr.next.prev = new_node
        curr.next = new_node


    # ----------------------------
    # DELETIONS
    # ----------------------------

    def delete_at_head(self):
        if not self.head:
            return
        self.head = self.head.next

        if self.head:
            self.head.prev = None

    def delete_at_tail(self):
        if not self.head:
            return
        
        if not self.head.next:
            self.head = None
            return

        curr=self.head
        while curr.next:
            curr=curr.next

        curr.prev.next = None

    def delete_at_position(self, pos: int):
        if not self.head:
            return
        
        if pos == 0:
            self.delete_head()
            return

        curr = self.head
        for _ in range(pos):
            if not curr:
                return  # out of range
            curr = curr.next

        if curr.prev:
            curr.prev.next = curr.next
        if curr.next:
            curr.next.prev = curr.prev
        
    # Delete FIRST OCCURRENCE of value
    def delete_value(self, target: int):
        curr = self.head
        
        if not curr:
            return

        # If head is the value
        if curr.val == target:
            self.delete_at_head()
            return

        while curr:
            if curr.val == target:
                if curr.prev:
                    curr.prev.next = curr.next
                if curr.next:
                    curr.next.prev = curr.prev
                return
            curr = curr.next

    def print_list(self):
        curr=self.head
        while curr:
            print(curr.val,end="->")
            curr=curr.next
        print("None")

ll= DoublyLL()
ll.insert_at_head(1)
ll.insert_at_head(2)
ll.insert_at_tail(3)

ll.insert_at_position(20,2)
ll.delete_at_head()
ll.delete_at_tail()
ll.delete_at_position(1)
ll.delete_value(1)
ll.print_list()