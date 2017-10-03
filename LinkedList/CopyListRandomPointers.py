"""
A linked list is given such that each node contains an additional 
random pointer which could point to any node in the list or null.

Return a deep copy of the list.

Note: This is a O(1) extra space approach (O(n) space required 
	  minimum as we need to return a deep copy)
"""

def copyRandomList(head):
    """
    :type head: RandomListNode
    :rtype: RandomListNode
    """
    if not head: return 
    node = head
    while node:
        copyNode = RandomListNode(node.label)
        copyNode.next = node.next
        node.next = copyNode
        node = copyNode.next
        # above logic can be reduce to the following pythonic statement
        # node.next, copyNode.next, node = copyNode, node.next, node.next
    node = head
    while node:
        if node.random: 
        	node.next.random = node.random.next
        node = node.next.next
    buffr = prev = RandomListNode('-1')
    node = head
    while node:
        prev.next = prev = node.next
        node.next = node = node.next.next
    return buffr.next