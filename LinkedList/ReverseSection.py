"""

Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

"""

def reverseBetween(head, m, n):
    """
    :type head: ListNode
    :type m: int
    :type n: int
    :rtype: ListNode
    """
    order = 1
    buffr = prev = ListNode(None)
    buffr.next = node = head
    M = prevM = None
    while order <= n:
        nxt = node.next
        if order == m: # at m, set M and prevM 
            prevM, M = prev, node
        elif order > m:
            node.next = prev # reverse
            if order == n: # at n adjust pointers 
                prevM.next, M.next = node, nxt
        order, node, prev = order + 1, nxt, node # update order & prev pntr, move node
    return buffr.next