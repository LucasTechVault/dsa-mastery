from typing import Optional

class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
        
def reorderList(head: Optional[ListNode]) -> None:
    # Guard clause - empty or single element list
    if not head or not head.next:
        return

    # 1. Find middle of Linked List
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    # 1.1 Split Linked List
    l2 = slow.next
    slow.next = None # split list
    
    # 2. Reverse L2
    prev = None
    cur = l2
    
    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    
    l2 = prev
    l1 = head
    
    # 3. Interweave merge
    while l2: # l2 will always be equal or smaller than l1
        t1 = l1.next
        t2 = l2.next
        
        l1.next = l2
        l2.next = t1
        
        l1 = t1
        l2 = t2
    