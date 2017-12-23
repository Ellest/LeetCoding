"""
Reverse a singly linked list.
"""

def reverseList(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    previous = None
    while head:
        head.next, head, previous = previous, head.next, head
    return previous