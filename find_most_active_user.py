'''
You’re analyzing a log file that records user actions throughout the day.
Each entry is represented by a user ID (string).
You need to find which user appeared the most times in the log.
'''

logs = [
    "alice", "bob", "alice",
    "dave", "bob", "alice",
    "carol", "bob", "bob"
]


def most_active_user(logs: list[str]) -> str:
    """
    Given a list of user IDs (strings),
    return the ID of the user who appears most frequently.
    If there’s a tie, return any one of them.
    """
    count = {}
    for i, j in enumerate(logs):
        name = logs[i]
        if count.get(name) is None:
            count[name] = 1
        if count.get(name) is not None:
            count[name] += 1
    # find the name with the highest count
    max_value = 0
    max_value_name = ''
    for count_of_names, name in enumerate(count):
        if max_value < count_of_names:
            max_value = count_of_names
            max_value_name = name
            return max_value_name
