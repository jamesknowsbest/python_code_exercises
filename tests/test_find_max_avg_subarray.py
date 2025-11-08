from find_max_avg_subarray import max_avg_subarray


def test_basic_array():
    ints = [1, 12, -5, -6, 50, 3]
    result = max_avg_subarray(ints, k=4)
    assert result == 12.75
