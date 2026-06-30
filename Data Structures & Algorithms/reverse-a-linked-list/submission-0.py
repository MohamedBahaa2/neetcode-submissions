# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        full_list = []
        if not head:
            return None
            
        while head:
            full_list.append(head)
            head = head.next

        for i in range(len(full_list) - 1, -1, -1):
            if i == 0:
                full_list[i].next = None
            else:
                full_list[i].next = full_list[i-1]

        return full_list[-1]
