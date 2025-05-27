# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        while head and head.next:
            slow = head
            fast = head.next

            prev.next = fast
            slow.next = fast.next
            fast.next = slow

            prev = slow
            head = slow.next
        return dummy.next