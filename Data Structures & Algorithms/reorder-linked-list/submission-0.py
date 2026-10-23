# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        arr = []
        cur = head
        while cur:
            arr.append(cur.val)
            cur = cur.next
        cur = head
        for i in range(len(arr)):
            if i % 2 == 1:
                real = len(arr) - 1 - i // 2
            else:
                real = i // 2
            cur.val = arr[real]
            cur = cur.next