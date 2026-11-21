import re

LOG_PATTERN = re.compile(
    r'(?P<ip>\S+) - - \[(?P<date>.*?)\] '
    r'"(?P<method>\S+) (?P<resource>\S+) (?P<protocol>.*?)" '
    r'(?P<status>\d+) (?P<size>\d+) '
    r'"(?P<referrer>.*?)" "(?P<agent>.*?)"'
    r'(?: (?P<time>\d+))?$'
)


def parse_line(line: str):
    match = LOG_PATTERN.match(line.strip())

    if not match:
        return None

    data = match.groupdict()

    data["status"] = int(data["status"])
    data["size"] = int(data["size"])

    if data["time"]:
        data["time"] = int(data["time"])

    return data


def parse_file(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        for line in file:
            parsed = parse_line(line)

            if parsed:
                yield parsed