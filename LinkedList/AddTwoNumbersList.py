"""

You are given two non-empty linked lists representing two non-negative integers. 
The most significant digit comes first and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading 
zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, 
reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7

"""

"""
# Method for getting length of a LL
"""
def base_10(head): 
    val = 0
    while head:
        val = val * 10 + head.val
        head = head.next
    return val
    
"""
# Main Method
"""
def addTwoNumbers(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """

    length1, length2 = length(l1), length(l2)
    longer = shorter = None
    if length1 > length2:
        longer, shorter = l1, l2
    else:
        longer, shorter = l2, l1
    diff = abs(length1 - length2)
    prev = None
    while longer: # create nodes. Add each position and disregard carries for now
        temp = ListNode(longer.val + (diff < 1 and shorter.val))
        temp.next, prev = prev, temp
        if diff < 1: shorter = shorter.next
        longer, diff = longer.next, diff - 1
    itr, prev, carry = prev, None, 0
    while itr: # reverse
        itr.val += carry
        carry = itr.val // 10
        itr.val %= 10
        itr.next, prev, itr = prev, itr, itr.next
    if carry: # if carry exists after reversal, create one extra node
        head = ListNode(1)
        prev.val %= 10
        head.next = prev
        return head
    return prev