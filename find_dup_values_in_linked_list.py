class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def de_dup(head_node: ListNode) -> ListNode:
    '''
    Use a set to track which values have been seen.
    Traverse the linked list with two pointers — one for the current node, and one for the previous node.
    If a duplicate is found, remove it by adjusting pointers.
    '''
    if head_node is None:
        return None
    unique_values = set()
    current_node = head_node
    previous_node = None

    while current_node is not None:
        if current_node.val in unique_values:
            # Duplicate found: skip current_node
            previous_node.next = current_node.next
            current_node = current_node.next
        else:
            # First time seeing this value: add to set
            unique_values.add(current_node.val)
            previous_node = current_node  # only move previous if the current is kept
            current_node = current_node.next  # move to next node
    return head_node


        
