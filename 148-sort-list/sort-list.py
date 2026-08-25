# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head):
        if not head or not head.next:
            return head

        # Find the middle
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Split the list
        second = slow.next
        slow.next = None

        # Sort both halves
        left = self.sortList(head)
        right = self.sortList(second)

        # Merge sorted halves
        return self.merge(left, right)

    def merge(self, left, right):
        dummy = ListNode(0)
        current = dummy

        while left and right:
            if left.val <= right.val:
                current.next = left
                left = left.next
            else:
                current.next = right
                right = right.next

            current = current.next

        if left:
            current.next = left

        if right:
            current.next = right

        return dummy.next