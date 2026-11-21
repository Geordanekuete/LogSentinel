from collections import Counter


class LogAnalyzer:

    def __init__(self):
        self.total_requests = 0
        self.invalid_lines = 0

        self.ip_counter = Counter()
        self.resource_counter = Counter()
        self.status_counter = Counter()

        self.response_times = []

    def process(self, entry):

        self.total_requests += 1

        self.ip_counter[entry["ip"]] += 1
        self.resource_counter[entry["resource"]] += 1
        self.status_counter[entry["status"]] += 1

        if entry.get("time") is not None:
            self.response_times.append(entry["time"])

    def get_average_response_time(self):

        if not self.response_times:
            return 0

        return round(
            sum(self.response_times) / len(self.response_times),
            2
        )

    def suspicious_ips(self):

        return [
            (ip, count)
            for ip, count in self.ip_counter.items()
            if count > 50
        ]