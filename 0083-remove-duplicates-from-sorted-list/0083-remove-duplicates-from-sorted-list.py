class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited = set()
        curr = head
        prev = None

        while curr:
            if curr.val in visited:
                prev.next = curr.next   # remove duplicate
            else:
                visited.add(curr.val)
                prev = curr
            curr = curr.next

        return head
