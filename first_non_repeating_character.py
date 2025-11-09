def first_unique_char(s: str) -> int:
    """
    Given a string s, return the index of the first non-repeating character.
    If it doesn’t exist, return -1. i.e leetcode should return 0
    """
    count = {}
    for index_position, char in enumerate(s):
        count[char] = count.get(char, 0) + 1
    for key, value in enumerate(s):
        # key is the index
        # value is the actual key of the dict
        if count[value] == 1:
            return key
    return -1


if __name__ == "__main__":
    print(first_unique_char("leetcode"))
