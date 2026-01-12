from collections import defaultdict

class APILatencyMonitor:
    def __init__(self):
        self.buckets = defaultdict(lambda: [0, 0, 0, 0])

    def process_request(self, endpoint, latency):
        if latency < 100:
            self.buckets[endpoint][0] += 1
        elif latency < 500:
            self.buckets[endpoint][1] += 1
        elif latency < 1000:
            self.buckets[endpoint][2] += 1
        else:
            self.buckets[endpoint][3] += 1

        self.print_counts(endpoint)

    def print_counts(self, endpoint):
        c = self.buckets[endpoint]
        print(f"{endpoint}: <100ms={c[0]}, <500ms={c[1]}, <1s={c[2]}, >1s={c[3]}")
        
if __name__ == "__main__":
    monitor = APILatencyMonitor()
    while True:
     try:
        line = input().strip()   # waits for next request
        if not line:
            continue

        _, endpoint, latency = line.split()
        monitor.process_request(endpoint, int(latency))

     except EOFError:
        break




    