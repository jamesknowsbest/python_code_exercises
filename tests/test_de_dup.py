from find_dup_values_in_linked_list import de_dup, ListNode

def test_de_dup():
    # Build the linked list: 3 -> 4 -> 3 -> 2 -> 6 -> 4 -> 2 -> 5
    n7 = ListNode(5)
    n6 = ListNode(2, n7)
    n5 = ListNode(4, n6)
    n4 = ListNode(6, n5)
    n3 = ListNode(2, n4)
    n2 = ListNode(3, n3)
    n1 = ListNode(4, n2)
    head = ListNode(3, n1)

    # Call the function
    new_head = de_dup(head)

    # Collect values from returned linked list
    result = []
    current = new_head
    while current:
        result.append(current.val)
        current = current.next

    # Assert the result is correct
    assert result == [3, 4, 2, 6, 5]
