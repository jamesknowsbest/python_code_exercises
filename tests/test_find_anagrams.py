from find_anagrams import group_anagrams_using_sort, group_anagrams_using_counts


def test_find_anagrams_using_sort():
    assert group_anagrams_using_sort(["eat", "tea", "tan", "ate", "nat", "bat"]) == [
        ["eat", "tea", "ate"],
        ["tan", "nat"],
        ["bat"],
    ]


def test_find_anagrams_using_count():
    assert group_anagrams_using_counts(["eat", "tea", "tan", "ate", "nat", "bat"]) == [
        ["eat", "tea", "ate"],
        ["tan", "nat"],
        ["bat"],
    ]
