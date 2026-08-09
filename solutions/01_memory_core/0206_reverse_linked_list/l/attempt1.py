def reverseLinkedList(head: Optional[ListNode]) -> Optional[ListNode]:
    prev, cur = None, head
    
    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
    
    return prev