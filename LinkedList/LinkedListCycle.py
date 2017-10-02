"""
Given a linked list, determine if it has a cycle in it.

Solve without extra space.
"""

def hasCycle(self, head):
    """
    :type head: ListNode
    :rtype: bool
    """
    if not head or not head.next: return False
    slow, fast = head.next, head.next.next
    while fast and fast.next and slow != fast:
        slow, fast = slow.next, fast.next.next
    return slow == fast