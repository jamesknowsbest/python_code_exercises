from log_filtering import filter_logs

def test_filter_logs():
    example_input = [
        "2025-11-19T10:00:00Z ERROR auth Login failed",
        "2025-11-19T10:00:01Z INFO api Request received",
        "2025-11-19T10:00:02Z ERROR api Timeout",
        "2025-11-19T10:00:03Z ERROR auth Invalid token"
    ]

    assert filter_logs(example_input) == {"auth": 2, "api": 1}