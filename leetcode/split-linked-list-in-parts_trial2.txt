# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        base_size, extra = divmod(length, k)

        result = []
        curr = head
        for i in range(k):
            part_head = curr
            part_size = base_size + (1 if i < extra else 0)

            for _ in range(part_size - 1):
                if curr:
                    curr = curr.next
            if  curr:
                next_node = curr.next
                curr.next = None
                curr = next_node
            result.append(part_head)
        return result
                


        
                
        
            

        