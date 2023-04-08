from collections import deque, defaultdict
import time

class DdosDetector:
    def __init__(self, time_window=60, request_limit=100):
        self.time_window = time_window
        self.request_limit = request_limit
        self.ip_request_count = defaultdict(deque)

    def _clean_old_requests(self, ip, current_time):
        while self.ip_request_count[ip] and self.ip_request_count[ip][0] - current_time > self.time_window:
            self.ip_request_count[ip].popleft()
    
    def log_request(self, ip, current_time):
        self._clean_old_requests(ip, current_time)
        self.ip_request_count[ip].append(current_time)


    def is_ddos_attack(self, ip, current_time):
        self._clean_old_requests(ip, current_time)
        return len(self.ip_request_count[ip]) > self.request_limit



def main():
    detector = DdosDetector(time_window=10, request_limit=100)
    ip_address = ['127.0.0.1', '192.168.1.2', '192.168.1.3']
    ddos_log = {ip: {"status": False, "attemps_over_threshold": 0} for ip in ip_address}
    for i in range(2999):
        ip = ip_address[i % len(ip_address)]
        current_time = time.time()
        detector.log_request(ip, current_time)
        if detector.is_ddos_attack(ip, current_time):
            # print(f'ip: {ip}, is_ddos_attack: {detector.is_ddos_attack(ip)}')
            ddos_log[ip]["status"] = True
            ddos_log[ip]["attemps_over_threshold"] += 1
            
        # if i % 10 == 0:
        #     print(f'ip: {ip}, is_ddos_attack: {detector.is_ddos_attack(ip)}')
    print("DDoS attack log: ", ddos_log)

if '__main__' == __name__:
    main()