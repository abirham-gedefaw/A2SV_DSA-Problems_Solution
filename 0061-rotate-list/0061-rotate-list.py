# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        length = 1
        curr = head
        while curr.next:
            curr = curr.next
            length += 1

        k %= length
        if k == 0:
            return head
            
        tail = head
        for _ in range(length - k - 1):
            tail = tail.next
        new_head = tail.next
        curr.next = head
        tail.next = None
        return new_head

        