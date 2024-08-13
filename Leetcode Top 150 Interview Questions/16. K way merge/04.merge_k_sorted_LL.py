# https://leetcode.com/problems/merge-k-sorted-lists/

class HeapNode:
    def __init__(self, node):
        self.node = node


class Solution:
    def mergeKLists(self, lists):
        dummy = ListNode(0)
        current = dummy
        heap = []

        # Initialize the heap
        for l in lists:
            if l:
                heapq.heappush(heap, HeapNode(l))

        # Extract the minimum node and add its next node to the heap
        while heap:
            heap_node = heapq.heappop(heap)
            node = heap_node.node
            current.next = node
            current = current.next
            if node.next:
                heapq.heappush(heap, HeapNode(node.next))

        return dummy.next