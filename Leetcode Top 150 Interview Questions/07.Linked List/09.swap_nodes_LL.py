#https://www.educative.io/courses/grokking-coding-interview-patterns-python/solution-swapping-nodes-in-a-linked-list

class LinkedListNode:
    # __init__ will be used to make a LinkedListNode type object.
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
class Soluton:
    def swap(node1, node2):
        temp = node1.data
        node1.data = node2.data
        node2.data = temp

    def swap_nodes(head, k):
        count = 0
        front, end = None, None
        curr = head

        while curr:
            count += 1
            if end is not None:
                end = end.next

            if count == k:
                front = curr
                end = head
            curr = curr.next

        swap(front, end)
        return head