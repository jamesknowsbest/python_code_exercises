from find_most_frequent_word import find_most_frequent_word

def test_find_most_frequent_word():
    assert find_most_frequent_word(["sun", "beach", "sun", "sand", "umbrella", "sun", "sand"]) == ("sun", 3)


def test_find_most_frequent_word_when_there_are_dups():
    assert find_most_frequent_word(["sun", "beach", "sun", "beach", "beach", "sun", "sand"]) == ("beach", 3)