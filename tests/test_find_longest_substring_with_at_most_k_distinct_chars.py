from find_longest_substring_with_at_most_k_distinct_chars import (
    find_longest_substring_with_at_most_k_distinct_chars,
)


def test_find_longest_substring_with_at_most_k_distinct_chars_aa():
    assert find_longest_substring_with_at_most_k_distinct_chars("aa", 1) == 2


def test_find_longest_substring_with_at_most_k_distinct_chars_aabbcc():
    assert find_longest_substring_with_at_most_k_distinct_chars("aabbcc", 2) == 4


def test_find_longest_substring_with_at_most_k_distinct_chars_aabcadcacacaca():
    assert (
        find_longest_substring_with_at_most_k_distinct_chars("abcadcacacaca", 3) == 11
    )
