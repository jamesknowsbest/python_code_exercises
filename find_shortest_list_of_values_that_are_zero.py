arr = [1, 2, -3, 3, -1, 2, -2]
# You need to find the longest contiguous sequence
# (a continuous “slice” of the array) that adds up to zero.
# In this example:
# [1, 2, -3] has a sum of 0 (length 3)
# [3, -1, 2, -2] also sums to 2 (not 0)
# [2, -3, 3, -1, 2, -2] sums to 1 (not 0)
# The longest that sums to 0 is length 3.

if __name__ == "__main__":
    print("starting to find longest contiguous sequence using:", arr)
    # itegrate through the array and keep track of the values
    prefix_sum = [0] * len(arr)
    print("init of prefix_sum", prefix_sum)
    prefix_sum[0] = arr[0]
    for i in range(len(arr)):
        if (i + 1) >= len(arr):
            break
        prefix_sum[i + 1] = arr[i] + arr[(i + 1)]
    print("population of prefix_sum", prefix_sum)