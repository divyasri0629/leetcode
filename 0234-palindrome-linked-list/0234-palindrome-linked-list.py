# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        original = []
        curr = head

        while curr:
            original.append(curr.val)
            curr = curr.next

        prev = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        curr = prev
        i = 0

        while curr:
            if original[i] != curr.val:
                return False
            i += 1
            curr = curr.next


        return True 