# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        prev = None
        curr = slow
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        left, right = head, prev
        max_twin_sum = 0
        while right:
            twin_sum = left.val + right.val
            max_twin_sum = max(max_twin_sum, twin_sum)
            left = left.next
            right = right.next
        return max_twin_sum


        
        