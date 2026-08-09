def hasCycles(head: Optional[ListNode]) -> bool:
    # Guard clause - empty list have no cycles
    if not head:
        return False
    
    slow = fast = head
    # need fast & fast.next since we have fast.next.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        # Any point slow == fast means cycle
        if slow == fast:
            return True
    
    # fast reached end, no cycle
    return False

    