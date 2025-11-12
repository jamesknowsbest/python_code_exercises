def find_most_frequent_ints(nums: [int], k: int) -> [int]:
    count = {}
    for i, integer in enumerate(nums):
        count[integer] = count.get(integer, 0) + 1
    buckets = [[] for _ in range(len(nums) + 1)]
    for key, value in count.items():
        buckets[value].append(key)
    result = []
    for i in range(len(buckets) - 1, 0, -1):
        for num in buckets[i]:
            result.append(num)
            if len(result) == k:
                return result

    return result
