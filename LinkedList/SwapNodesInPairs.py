"""
Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. 
You may not modify the values in the list, only nodes itself can be changed.
"""

def swapPairs(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    buffr = prev = ListNode(None)
    prev.next = head
    while head and head.next:
        nxt = head.next.next
        head.next.next = head # reverse pointer
        prev.next = head.next # set earlier pair's next to node.next
        prev = head # update previous
        head.next = head = nxt
    return buffr.next

def swapPairs_pythonic(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    buffr = prev = ListNode(None)
    prev.next = head
    while head and head.next:
        head.next.next, prev.next, head.next, prev, head = \
            head, head.next, head.next.next, head, head.next.next
    return buffr.next