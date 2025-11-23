from collections import deque
from datetime import datetime
requests = {}

'''
A token is added to the bucket every 1 / r seconds.
The bucket can hold at the most b tokens. If a token arrives when the bucket is full, it is discarded.
When a packet (network layer PDU) of n bytes arrives,
if at least n tokens are in the bucket, n tokens are removed from the bucket, and the packet is sent to the network.
if fewer than n tokens are available, no tokens are removed from the bucket, and the packet is considered to be non-conformant.
'''
def refill_bkt(user_id: str, timestamp: datetime, rate: float, max_tokens: int = 10):
    now = datetime.now()
    if requests.get(user_id) is None:
        requests[user_id] = { "user_id": user_id }
        requests[user_id]["last_request_date"] = now
    elasped_seconds = (now - requests[user_id]["last_request_date"]).total_seconds()
    requests[user_id]["last_request_date"] = timestamp
    requests[user_id]["max_tokens"] = max_tokens
    tokens_to_add = elasped_seconds * rate
    requests[user_id]["tokens"] = min(requests.get(user_id).get("tokens", 10) + tokens_to_add, requests[user_id]["max_tokens"])

def allow_request(user_id: str, timestamp: datetime, tokens_used: int = 1) -> bool:    
    # refill bucket
    refill_bkt(user_id=user_id, timestamp=timestamp, rate=1.0)
    # check if there are enough tokens
    if requests[user_id]["tokens"] >= tokens_used:
        requests[user_id]["tokens"] -= tokens_used
        return True
    return False