"""

Given a linked list and a value x, partition it such that all 
nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes 
in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.

"""    

def partition(head, x):
    """
    :type head: ListNode
    :type x: int
    :rtype: ListNode
    """
    if not head: return head
    length = 1
    end = head
    while end.next: # count # of nodes while locating the end of list
        end, length = end.next, length + 1
    buffr = prev = ListNode(None)
    prev.next = itr = head
    while length:
        nxt = itr.next
        if itr.val >= x and itr != end: # move to end. skip if node is already at end
            prev.next, end.next, end = itr.next, itr, itr
            itr.next = None
        else: # if not, update previous pointer
            prev = itr
        itr, length = nxt, length - 1 # move node and update remaining length
    return buffr.next