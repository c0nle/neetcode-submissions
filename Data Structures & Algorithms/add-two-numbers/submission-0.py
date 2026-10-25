# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = dummy = ListNode()
        cur1, cur2 = l1, l2
        rest = 0
        while cur1 and cur2:
            val = cur1.val + cur2.val + rest
            res.next = ListNode(val%10)
            rest = math.ceil(val // 10)
            cur1 = cur1.next
            cur2 = cur2.next
            res = res.next
        
        while cur1:
            val = cur1.val + rest
            res.next = ListNode(val%10)
            rest = math.ceil(val // 10)
            cur1 = cur1.next
            res = res.next
        
        while cur2:
            val = cur2.val + rest
            res.next = ListNode(val%10)
            rest = math.ceil(val // 10)
            cur2 = cur2.next
            res = res.next
        
        if rest > 0:
            res.next = ListNode(rest)
        
        return dummy.next