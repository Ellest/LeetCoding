"""
Merge two sorted linked lists and return it as a 
new list. The new list should be made by splicing 
together the nodes of the first two lists.
"""

def mergeTwoLists(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    buffr = itr = ListNode(None)
    while l1 and l2:
        if l1.val <= l2.val:
            itr.next = ListNode(l1.val)
            l1 = l1.next
        else:
            itr.next = ListNode(l2.val)
            l2 = l2.next
        itr = itr.next
    itr.next = l1 or l2
    return buffr.next