def find_longest_substring_with_at_most_k_distinct_chars(
    string_of_chars: str, num_of_distinct_chars: int
) -> int:
    max_length = 0
    start_position = 0
    counts = {}
    for end_position, ch in enumerate(string_of_chars):
        counts[ch] = counts.get(ch, 0) + 1
        while len(counts) > num_of_distinct_chars:
            # adjust the starting position and
            # remove the characters that are no longer in the window
            start_char = string_of_chars[start_position]
            counts[start_char] -= 1
            if counts[start_char] == 0:
                del counts[start_char]
            start_position += 1
        max_length = max(max_length, end_position - start_position + 1)
    return max_length
