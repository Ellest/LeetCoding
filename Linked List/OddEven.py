"""
Given a singly linked list, group all odd nodes together followed by the even nodes. 
Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity 
and O(nodes) time complexity.

Example:
Given 1->2->3->4->5->NULL,
return 1->3->5->2->4->NULL.
"""


def oddEvenList(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if not head: return head
    length = 1 
    end = head
    while end.next:
        length, end = length + 1, end.next
    if length < 3: return head # length < 3 will not change
    even, order = False, 1
    prev = node = head # initialize pointer to head
    while order <= length:
        temp = node.next
        if even: # move node to back then reset end reference to node
            prev.next, end.next, end = node.next, node, node
            node.next = None
        else: # update "previous"
            prev = node
        node, even, order = temp, not even, order + 1 # increment order & toggle even
    return head