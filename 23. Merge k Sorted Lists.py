import heapq


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        heap = []

        class HeapEntry(object):
            def __init__(self, node, index):
                self.node = node
                self.index = index

            def __lt__(self, other):
                return self.node.val < other.node.val

        for i, l in enumerate(lists):
            if l:
                heapq.heappush(heap, HeapEntry(l, i))

        dummy = ListNode(0)
        current = dummy

        while heap:
            entry = heapq.heappop(heap)
            node = entry.node
            current.next = node
            current = current.next

            if node.next:
                heapq.heappush(heap, HeapEntry(node.next, entry.index))

        return dummy.next