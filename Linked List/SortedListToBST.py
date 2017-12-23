"""

Given a singly linked list where elements are sorted in ascending 
order, convert it to a height balanced BST.

Using the length of the list, we can generate nodes mimicing the
list to BST conversion algorithm of taking halves and recursively
creating childs with left and right partitions at the level. Twist 
is that since we know we'll be creating the tree starting with the 
left most child and go up from there in an order identical to an 
inorder traversal (due to the DFS nature of the conversion) we just
need to keep track of where we are in the LinkedList and move the
pointer to the next node whenever we create a TreeNode.

"""


def createTree(l, h, refHead):
    if l > h: return 
    m = l + (h-l) // 2
    left = createTree(l, m-1, refHead)
    root = TreeNode(refHead[0].val)
    root.left = left
    refHead[0] = refHead[0].next # move node
    root.right = createTree(m+1, h, refHead)
    return root

def lengthLL(head):
    l = 0
    while head:
        length, head = length + 1, head.next

def sortedListToBST(head):
    """
    :type head: ListNode
    :rtype: TreeNode
    """
    length = lengthLL(head)
    if not length: return # empty list
    return createTree(0, length-1, [head])