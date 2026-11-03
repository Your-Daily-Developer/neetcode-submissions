class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fast = slow = dummy

        # Step 1: Move fast n steps ahead
        for _ in range(n):
            fast = fast.next

        # Step 2: Move both until fast reaches the last node
        while fast.next:
            slow = slow.next
            fast = fast.next

        # Step 3: Skip the target node
        slow.next = slow.next.next

        return dummy.next   