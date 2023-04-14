i# Import required modules
import time
from collections import defaultdict, deque

class DdosDetector:
    """
    Design a DDoS detector that can detect if a single IP is making more than 100 requests per minute (60 seconds).
    """

    def __init__(self, time_window: int = 60, request_limit: int = 100):
        self.time_window = time_window        # The time window (in seconds) to check for DDoS attacks
        self.request_limit = request_limit    # The maximum number of requests allowed within the time window
        self.ip_request_count = defaultdict(deque)  # A dictionary storing the request timestamps for each IP

    # Helper method to clean up old requests outside the time window for a given IP.
    def _clean_old_requests(self, ip, current_time):
        while self.ip_request_count[ip] and self.ip_request_count[ip][0] < current_time - self.time_window:
            self.ip_request_count[ip].popleft()

    # Public method to log a request from a given IP.
    def log_request(self, ip: str):
        current_time = time.time()
        self._clean_old_requests(ip, current_time)
        self.ip_request_count[ip].append(current_time)
    
    # Public method to check if a given IP is involved in a DDoS attack.
    def is_ddos_attack(self, ip: str) -> bool:
        current_time = time.time()
        self._clean_old_requests(ip, current_time)
        return len(self.ip_request_count[ip]) > self.request_limit

# Main function to test the DdosDetector class
def main():
    detector = DdosDetector(time_window=60, request_limit=100)
    ip_address = ['127.0.0.1', '192.168.1.2', '192.168.1.3']

    ddos_log = {ip: {'status': False, 'Over_threhold_attack': 0} for ip in ip_address}

    for i in range(3000):
        ip = ip_address[i % len(ip_address)]
        detector.log_request(ip)
        if detector.is_ddos_attack(ip):
            ddos_log[ip]['status'] = True
            ddos_log[ip]['Over_threhold_attack'] += 1
        
    print(f"Ddos attack log: {ddos_log}")


if '__main__' == __name__:
    main()