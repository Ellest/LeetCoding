"""
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
"""


def deleteDuplicates(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    previous = None
    itr = head
    while itr:
        temp = itr.next
        if previous and itr.val == previous.val:
            previous.next, itr.next = itr.next, None
        else:
            previous = itr
        itr = temp
    return head