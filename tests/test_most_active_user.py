from find_most_active_user import most_active_user


def test_single_most_active_user():
    logs = ["alice", "bob", "alice", "carol", "bob", "bob"]
    result = most_active_user(logs)
    assert result == "bob"


def test_all_unique_users():
    logs = ["alice", "bob", "carol"]
    result = most_active_user(logs)
    # Any of them is fine, since all appear once
    assert result in ["alice", "bob", "carol"]


def test_empty_list():
    logs = []
    result = most_active_user(logs)
    # depending on your function design, could return None
    assert result is None


def test_tie_between_users():
    logs = ["alice", "bob", "alice", "bob"]
    result = most_active_user(logs)
    assert result in ["alice", "bob"]
