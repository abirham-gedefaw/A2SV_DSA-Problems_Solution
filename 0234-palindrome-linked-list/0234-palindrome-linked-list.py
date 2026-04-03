# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        reverse_half = None
        curr = slow
        while curr:
            temp = curr.next
            curr.next = reverse_half
            reverse_half = curr
            curr = temp

        left, right = head, reverse_half
        while right:
            if left.val != right.val:
                return False
                
            left = left.next
            right = right.next
        # before return the result restoring the orginal list is vital.
        restore = None
        curr = reverse_half
        while curr:
            temp = curr.next
            curr.next = restore
            restore = curr
            curr = temp
        return True



        