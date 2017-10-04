"""

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

"""

def mergeKLists(lists):
    """
    :type lists: List[ListNode]
    :rtype: ListNode
    """
    minHeap = []
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(minHeap, (node.val, i))
    buffr = itr = ListNode(None)
    while minHeap:
        value, i = heapq.heappop(minHeap)
        itr.next = itr = lists[i]
        if itr.next:
            lists[i] = lists[i].next
            heapq.heappush(minHeap, (lists[i].val, i))
    return buffr.next