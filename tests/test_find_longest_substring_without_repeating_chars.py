from find_longest_substring_without_repeating_chars import (
    find_longest_substring_without_repeating_chars,
)


def test_find_longest_substring_without_repeating_chars_abcabcbb():
    assert find_longest_substring_without_repeating_chars("abcabcbb") == 3


def test_find_longest_substring_without_repeating_chars_bbbbb():
    assert find_longest_substring_without_repeating_chars("bbbbb") == 1


def test_find_longest_substring_without_repeating_chars_pwwkew():
    assert find_longest_substring_without_repeating_chars("pwwkew") == 3


def test_find_longest_substring_without_repeating_chars_abcde():
    assert find_longest_substring_without_repeating_chars("abcde") == 5
