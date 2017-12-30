 def sortList(head):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def merge(head1, head2):
            buffr = prev = ListNode(None)
            while head1 and head2:
                if head1.val < head2.val:
                    prev.next = prev = head1
                    head1 = head1.next
                else:
                    prev.next = prev = head2
                    head2 = head2.next
            prev.next = head1 or head2
            return buffr.next
        
        def sorter(head):
            if not head.next:
                return head
            slow, fast = head, head.next
            while fast and fast.next and fast.next.next:
                slow, fast = slow.next, fast.next.next
            temp, slow.next = slow.next, None
            left = sorter(head)
            right = sorter(temp)
            return merge(left, right)                
                
        if not head:
            return None
        return sorter(head)