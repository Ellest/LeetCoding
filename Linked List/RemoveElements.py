"""
Remove all elements from a linked list of integers 
that have value val.

Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5
"""

def removeElements(head, val):
    """
    :type head: ListNode
    :type val: int
    :rtype: ListNode
    """
    buffr = prev = ListNode(None)
    buffr.next = head
    while head:
        temp = head.next
        if head.val == val:
            prev.next, head.next = head.next, None
        else:
            prev = head
        head = temp
    return buffr.next