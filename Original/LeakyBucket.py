import time 
from collections import deque

class LeakyBucket:
    """
    Simulates the leak by removing elements from the bucket based on the leak rate.
    It calculates the time elapsed since the last leak and updates the bucket accordingly.
    """
    
    def __init__(self, leak_rate, capacity):
        self.leak_rate = leak_rate       # Rate at which the bucket leaks
        self.capacity = capacity         # Maximum capacity of the bucket
        self.bucket = deque()            # Deque to represent the bucket
        self.last_leak_time = time.time()  # Time of the last leak

    # Simulate the leak by removing elements from the bucket based on the leak rate
    def leak(self):
        current_time = time.time()
        time_elapsed = current_time - self.last_leak_time
        leak_amount = int(time_elapsed * self.leak_rate)

        while leak_amount > 0 and len(self.bucket) > 0:
            request_time = self.bucket[0]
            if request_time <= leak_amount:
                leak_amount -= request_time
                self.bucket.popleft()
            else:
                self.bucket[0] -= leak_amount
                leak_amount = 0

        self.last_leak_time = current_time

    # Check if a request is allowed by the leaky bucket algorithm
    def allow_request(self):
        self.leak()
        if sum(self.bucket) + 1 <= self.capacity:
            self.bucket.append(1)
            return True
        else:
            return False
        

def main():
    rate_limit = LeakyBucket(leak_rate=2, capacity=5)  # 1 token per second, bucket capacity of 5 tokens

    requests = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 1.5, 1.6, 1.7, 1.8, 1.9]  # Requests arriving at different times

    start_time = time.time()
    for request_time in requests:
        while time.time() - start_time < request_time:
            # Wait until request time hits
            pass
        
        if rate_limit.allow_request():
            print(f"Request at time {request_time:.1f} allowed.")
        else:
            print(f"Request at time {request_time:.1f} denied. Rate limit exceeded.")


    


if __name__ == "__main__":
    main()