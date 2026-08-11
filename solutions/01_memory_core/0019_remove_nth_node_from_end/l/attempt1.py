from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
def removeNthNodeFromEnd(head: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(val=0, next=head)
    front = end = dummy
    
    # 1. Advance front ptr by n steps
    for _ in range(n):
        front = front.next
    
    # 2. Advance front & back in tandem until front reach end
    while front.next: # to ensure end node is 1 step before
        front = front.next
        end = end.next
    
    # 3. At this instant, end is 1 step behind the nth-node from end
    end.next = end.next.next
    
    return dummy.next