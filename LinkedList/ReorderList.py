"""

Given a singly linked list L: L_0 -> L_1 -> … -> L_n-1 -> L_n,
reorder it to: L_0 -> L_n -> L_1 -> L_n-1 -> L_2 -> L_n-2 ->…

You must do this in-place without altering the nodes' values.

For example,

Given {1,2,3,4}, reorder it to {1,4,2,3}.

"""

def reorderList(head):
    """
    :type head: ListNode
    :rtype: void Do not return anything, modify head in-place instead.
    """
    if not head or not head.next: return
    slow, fast = head.next, head.next.next
    while fast and fast.next: # find mid point
        slow, fast = slow.next, fast.next.next
    mid = prev = slow # initialize setup
    slow = slow.next # move slow into reverse region
    while slow: # reverse latter half
        slow.next, prev, slow = prev, slow, slow.next
    while prev != mid: # reset pointers moving in 
        nxtHead, nxtEnd = head.next, prev.next
        head.next, prev.next = prev, head.next
        head, prev = nxtHead, nxtEnd
    mid.next = None # mid is the middle pivot so set end pointer to None