# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head or not head.next or k == 0:
            return head

        # Find the length and tail
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        k %= length
        if k == 0:
            return head

        # Find new tail at (length - k - 1)
        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next

        # Rearranging pointers
        new_head = new_tail.next
        new_tail.next = None
        tail.next = head

        return new_head