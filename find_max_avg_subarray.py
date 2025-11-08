def max_avg_subarray(ints, k):
    sum_array_averages = []
    i = 0
    while (i + k) <= len(ints):
        # get all elements from the starting marker to k
        sum_array = ints[i : i + k]
        # computer avg
        sum = 0
        for m, n in enumerate(sum_array):
            sum += n
        sum_array_avg = sum / k
        sum_array_averages.append(sum_array_avg)
        i += 1
    return max(sum_array_averages)


if __name__ == "__main__":
    print(max_avg_subarray([1, 12, -5, -6, 50, 3], 4))
