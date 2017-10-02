"""
Reverse Doubly Linked List
"""

def reverseDouble(head):
	previous = None
	while head:
		temp = head.next
		head.next = previous
		if previous:
			previous.prev = head
		head = temp
	return previous