# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: ListNode | None) -> ListNode | None:
        stack = []
        cur = head

        while cur:
            while stack and stack[-1].val < cur.val:
                stack.pop()
                
            stack.append(cur)
            cur = cur.next

        head = stack[0]
        cur = head

        for i in range(1, len(stack)):
            cur.next = stack[i]
            cur = cur.next

        #cur.next = None
        return head