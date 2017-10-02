"""
Write a function to delete a node (except the tail) in a singly linked 
list, given only access to that node.

"""

def deleteNode(node):
    """
    :type node: ListNode
    :rtype: void Do not return anything, modify node in-place instead.
    """
    if node:
        if not node.next:
            node.val = None
        else:
            node.val = node.next.val
            node.next.next, node.next = None, node.next.next