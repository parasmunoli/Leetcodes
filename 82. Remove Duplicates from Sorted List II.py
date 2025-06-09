# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0, head)
        prev = dummy
        curr = head

        while curr:
            if curr.next and curr.val == curr.next.val:
                duplicate_val = curr.val
                while curr and curr.val == duplicate_val:
                    curr = curr.next
                prev.next = curr
            else:
                prev = prev.next
                curr = curr.next

        return dummy.next