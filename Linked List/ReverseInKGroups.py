"""

Given a linked list, reverse the nodes of a linked list k at a 
time and return its modified list.

k is a positive integer and is less than or equal to the length of 
the linked list. If the number of nodes is not a multiple of k then 
left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may 
be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5


"""

def reverseKGroup(head, k):
    """
    :type head: ListNode
    :type k: int
    :rtype: ListNode
    """
    if not head or k < 2: return head
    buffr = prev = ListNode(None)
    prev.next = start = head
    cntr = C = k-1
    while head:
        if not cntr: # reverse segment of k nodes
        	# set next of last segment's end to current node
            prev.next, prev = head, start 
            before, itr, start = start, start.next, head.next # setup for reversal
            while itr != start: # reverse nodes
                itr.next, before, itr = before, itr, itr.next
            head, cntr = start, C # set up next segment
            # initialize next of current segment's end to the beginning of next segment
            prev.next = head 
        else:
            head, cntr = head.next, cntr - 1
    return buffr.next