from find_distance_in_next_largest_int import find_next_largest_int

def test_find_next_largest_int():
    assert find_next_largest_int([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]