from first_non_repeating_character import first_unique_char


def test_leetcode():
    assert first_unique_char("leetcode") == 0


def test_loveleetcode():
    assert first_unique_char("loveleetcode") == 2


def test_laabbcc():
    assert first_unique_char("aabbcc") == -1
