from token_bucket import allow_request
from datetime import datetime

def test_allow_request():
    assert(allow_request("james", datetime.now())) == True
    assert(allow_request("james", datetime.now())) == True
    assert(allow_request("james", datetime.now())) == True
    assert(allow_request("james", datetime.now())) == True
    assert(allow_request("james", datetime.now())) == True
    assert(allow_request("james", datetime.now())) == True
    assert(allow_request("james", datetime.now())) == True
    assert(allow_request("james", datetime.now())) == True
    assert(allow_request("james", datetime.now())) == True
    assert(allow_request("james", datetime.now())) == True
    assert(allow_request("james", datetime.now())) == False # this is the 11 request in a short period with a refill rate of 1 token per second, should be false
    assert(allow_request("james", datetime.now())) == False # as well as this one
    assert(allow_request("james", datetime.now())) == False # and this one