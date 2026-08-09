from typing import Optional

def mergeTwoLists(
    list1: Optional[ListNode],
    list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # 1. Handle edge cases
        # 1.1 Both empty
        if not list1 and not list2:
            return None

        # 1.2 list1 empty
        if not list1:
            return list2
    
        # 1.3 list2 empty
        if not list2:
            return list1

        # 2 Perform merge
        result = ListNode()
        cur = result
        
        while list1 and list2:
            if list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next
            
            else:
                cur.next = list2
                list2 = list2.next
            
            cur = cur.next
        
        # 3. Handle leftovers
        if list1:
            cur.next = list1
        if list2:
            cur.next = list2
        
        return result.next
        