import time
import math
class TokenBucket:
    """
    Token Bucket:

    1. The token bucket algorithm maintains a "bucket" of tokens, with a specified capacity.
    2. Tokens are added to the bucket at a specific rate (e.g., 1 token per second) up to the bucket's capacity.
    3. When a request comes in, a token is removed from the bucket. If there are no tokens left, the request is denied.
    4. Token bucket allows for short bursts in traffic, as long as there are enough tokens in the bucket.
    5. The token bucket algorithm is generally smoother than the leaky bucket algorithm in handling incoming requests.
    
    """
    def __init__(self, rate, capacity):
        self.rate = rate                     # Rate at which tokens are added to the bucket
        self.capacity = capacity             # Maximum capacity of the bucket
        self.tokens = capacity               # Current number of tokens in the bucket
        self.last_time_to_fill = time.perf_counter()  # Time of the last token refill

    # Refill the token bucket based on the elapsed time and refill rate
    def refill_bucket(self):
        current_time = time.perf_counter()
        time_elapsed = current_time - self.last_time_to_fill
        tokens_to_fill = math.floor(time_elapsed * self.rate)
        self.tokens = min(self.tokens + tokens_to_fill, self.capacity)
        self.last_time_to_fill = current_time if tokens_to_fill > 0 else self.last_time_to_fill

    # Check if a request is allowed by the token bucket algorithm
    def ok_request(self):
        self.refill_bucket()
        if self.tokens >= 1:
            self.tokens -= 1
            return True
        else:
            return False

def main():
    rate_limit = TokenBucket(rate=2, capacity=5)  # 1 token per second, bucket capacity of 5 tokens

    requests = [0.1, 0.2, 0.3, 0.4, 0.5, 1.5, 1.6, 1.7, 1.8, 1.9]  # Requests arriving at different times

    start_time = time.perf_counter()
    for request_time in requests:
        while time.perf_counter() - start_time < request_time:
            # Wait until request time hits
            pass
        
        if rate_limit.ok_request():
            print(f"at {request_time}, with {rate_limit.tokens}")
            print(f"Request at time {request_time:.1f} allowed.")
        else:
            print(f"Request at time {request_time:.1f} denied. Rate limit exceeded.")


    


if __name__ == "__main__":
    main()