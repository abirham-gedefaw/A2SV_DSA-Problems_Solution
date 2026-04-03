# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        ans=dummy
        list1=l1
        list2=l2
        rem=0
        while rem or list1 or list2:
            sums=rem
            if list1:
                sums+=list1.val
                list1=list1.next
            if list2:
                sums+=list2.val
                list2=list2.next
            if sums>9:
                sums-=10
                rem=1
            else:
                rem=0
            news=ListNode(sums)
            ans.next=news
            ans=news
        return dummy.next
        

        