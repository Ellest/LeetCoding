"""
Given a sorted linked list, delete all nodes that have duplicate numbers, 
leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.

"""


def deleteDuplicates(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    buffr = prev = ListNode(None)
    buffr.next = itr = head
    val = None
    while itr:
        nxt = itr.next
        if itr.val == val or (itr.next and itr.next.val == itr.val):
            prev.next, itr.next = itr.next, None
        else:
            prev = itr
        itr, val = nxt, itr.val
    return buffr.next