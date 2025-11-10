def find_longest_substring_without_repeating_chars(string_of_chars: str) -> int:
    max_length = 0
    start = 0
    positions = {}
    for i, ch in enumerate(string_of_chars):
        if ch in positions and positions[ch] >= start:
            start = positions[ch] + 1
        positions[ch] = i
        max_length = max(max_length, i - start + 1)
    return max_length
