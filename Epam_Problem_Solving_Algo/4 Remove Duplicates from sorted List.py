class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head: ListNode) -> ListNode:
    # If the list is empty or has only one node, no duplicates exist
    if not head or not head.next:
        return head
    
    current = head
    
    # Traverse the list until the second-to-last node
    while current and current.next:
        if current.val == current.next.val:
            # Skip the duplicate node
            current.next = current.next.next
        else:
            # Move to the next unique node
            current = current.next
            
    return head
  """ 100 % passes """
