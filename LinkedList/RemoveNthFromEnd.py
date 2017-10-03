"""
Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.
"""

def removeNthFromEnd(head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    buffr = prev = ListNode(None)
    prev.next = left = right = head
    while n:
        right, n = right.next, n - 1
    while right:
        prev = left
        left, right = left.next, right.next
    # delete node
    prev.next, left.next = left.next, None
    return buffr.next