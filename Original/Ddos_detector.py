import time
from collections import defaultdict, deque

class DdosDetector:
    """
    Design a DDoS detector that can detect if a single IP is making more than 100 requests per minute (60 seconds).
    
    """

    def __init__(self, time_window: int = 60, request_limit: int = 100):
        self.time_window = time_window
        self.request_limit = request_limit
        self.ip_request_count = defaultdict(deque)

    def _clean_old_requests(self, ip, current_time):
        while self.ip_request_count[ip] and self.ip_request_count[ip][0] < current_time - self.time_window:
            self.ip_request_count[ip].popleft()

    def log_request(self, ip: str):
        current_time = time.time()
        self._clean_old_requests(ip, current_time)
        self.ip_request_count[ip].append(current_time)
    
    def is_ddos_attack(self, ip: str) -> bool:
        current_time = time.time()
        self._clean_old_requests(ip, current_time)
        return len(self.ip_request_count[ip]) > self.request_limit


def main():
    detector = DdosDetector(time_window=60, request_limit=100)
    ip_address = ['127.0.0.1', '192.168.1.2', '192.168.1.3']

    ddos_log = {ip: {'status': False, 'Over_threhold_attack': 0} for ip in ip_address}

    for i in range(3000):
        ip = ip_address[i % len(ip_address)]
        detector.log_request(ip)
        if detector.is_ddos_attack:
            ddos_log[ip]['status'] = True
            ddos_log[ip]['Over_threhold_attack'] += 1
        
    print(f"Ddos attack log: {ddos_log}")


if '__main__' == __name__:
    main()