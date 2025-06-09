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
        currNode = head
        while currNode and currNode.next:
            if currNode.val == currNode.next.val:
                currNode.next = currNode.next.next
            else:
                currNode = currNode.next
        return head
