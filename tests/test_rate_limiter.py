from rate_limiter import allow_request

def test_allow_request():
    assert(allow_request("alice", 1))  == True
    assert(allow_request("alice", 2))  == True
    assert(allow_request("alice", 3))  == True
    assert(allow_request("alice", 4))  == False
    assert(allow_request("alice", 12)) == True