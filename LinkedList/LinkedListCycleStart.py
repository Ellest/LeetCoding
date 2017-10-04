"""
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Note: Do not modify the linked list.
"""


def detectCycle(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if not head or not head.next: return 
    slow, fast = head.next, head.next.next
    while fast and fast.next and slow != fast:
        slow, fast = slow.next, fast.next.next
    if not fast or not fast.next: return 
    itr = head
    while slow != itr:
        itr, slow = itr.next, slow.next
    return slow