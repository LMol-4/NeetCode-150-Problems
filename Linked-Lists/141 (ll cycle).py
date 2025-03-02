# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # brute force
        """current = head
        previous = []
        while current:
            if current in previous:
                return True
            previous.append(current)
            current = current.next
            
            
        return False"""

        # low memory
        """current = head
        while current:
            if current.val == current.next:
                return True
            
            current.val = current.next
            current = current.next

        return False"""

        # dictionary - fast runtime, bad mem
        """history = {}
        current = head
        while current:
            history[current] = 1 + history.get(current, 0)
            if history[current] > 1:
                return True
            current = current.next
        
        return False"""

        # fast slow pointer
        fast = head
        slow = head
        
        while fast:
            fast = fast.next
            if fast == slow:
                return True
            
            if fast:
                fast = fast.next
            slow = slow.next

        return False