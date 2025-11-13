def merge_sort(input: list[int]) -> list[int]:
    if len(input) <= 1:
        return input
    mid = len(input) // 2
    left_side_split_list = merge_sort(input[:mid])
    right_side_split_list = merge_sort(input[mid:])
    i = j = 0
    result = []
    while i < len(left_side_split_list) and j < len(right_side_split_list):
        if left_side_split_list[i] < right_side_split_list[j]:
            result.append(left_side_split_list[i])
            i += 1
        else:
            result.append(right_side_split_list[j])
            j += 1
    result.extend(left_side_split_list[i:])
    result.extend(right_side_split_list[j:])
    return result
