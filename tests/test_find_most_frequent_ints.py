from find_k_most_frequent_ints import find_most_frequent_ints


def test_find_most_frequent_ints_one_num():
    assert find_most_frequent_ints([1], 1) == [1]


def test_find_most_frequent_ints_multiple_nums():
    assert find_most_frequent_ints([1, 1, 1, 2, 2, 3], 2) == [1, 2]


# def test_find_most_frequent_ints_multiple_nums_higher_k_value():
#     assert find_most_frequent_ints(
#         [1, 1, 1, 2, 2, 3, 5, 5, 6, 6, 3, 2, 1, 23, 34, 45, 5, 6, 6, 4, 3, 2, 2], 20
#     ) == [1, 2]
