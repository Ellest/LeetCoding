"""
Write a program to find the node at which the intersection of two singly linked lists begins.
"""

def getIntersectionNode(headA, headB):
    """
    :type head1, head1: ListNode
    :rtype: ListNode
    """
    if not headA or not headB: return None
    A, B = headA, headB
    while A != B:
        A = headB if not A else A.next
        B = headA if not B else B.next
    return A