"""

Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.

"""

def rotateRight(head, k):
    """
    :type head: ListNode
    :type k: int
    :rtype: ListNode
    """
    length = 0
    node = head
    while node:
        length, node = length + 1, node.next
    if length < 2: return head
    adjusted_k = k % length
    if not adjusted_k: return head
    left = right = head 
    while adjusted_k:
        right, adjusted_k = right.next, adjusted_k - 1
    while right.next:
        left, right = left.next, right.next
    return_head, left.next, right.next = left.next, None, head
    return return_head