class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # First pass: count nodes
        count = 0
        temp = head
        while temp:
            count += 1
            temp = temp.next

        # Find middle index
        mid = count // 2

        # Second pass: move to middle
        temp = head
        for _ in range(mid):
            temp = temp.next

        return temp
