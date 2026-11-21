# 🛡️ LogSentinel

> High-performance log analysis and monitoring tool written in Python.

LogSentinel is a command-line log analysis tool designed to process large web server logs efficiently. It parses Apache/Nginx-style access logs, extracts meaningful statistics, detects suspicious activity patterns, and exports detailed reports in CSV format.

Built with performance and simplicity in mind, LogSentinel can analyze log files line-by-line without loading entire files into memory, making it suitable for very large datasets.

---

## ✨ Features

- Fast streaming log parsing
- Large file support
- Apache/Nginx access log analysis
- Invalid line detection
- Top client identification
- Top requested resource analysis
- HTTP status code statistics
- Response time analysis
- Suspicious activity detection
- CSV report generation
- Clean command-line interface
- ASCII startup banner

---

## 📁 Project Structure

```text
LogSentinel/
│
├── main.py
├── parser.py
├── analyzer.py
├── report.py
├── banner.py
│
├── logs/
├── reports/
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## 🚀 Usage

Run LogSentinel against a log file:

```bash
python main.py access.log
```

---

## Example Output

```text
=================================================
FILE ANALYSIS
=================================================

Total Requests : 1500000

Average Response Time : 13.4 ms

Top Clients

192.168.0.10       15423
10.0.0.5           12087
172.16.0.3          8764

Report saved : reports/log_report.csv
```

---

## Supported Log Format

Example:

```text
192.168.0.10 - - [12/Feb/2024:10:15:32 +0300] "GET /index.html HTTP/1.1" 200 532 "-" "Mozilla/5.0" 12
```

Captured fields:

- Client IP
- Timestamp
- HTTP Method
- Requested Resource
- Protocol
- Status Code
- Response Size
- User Agent
- Processing Time

---

## CSV Reporting

After analysis, LogSentinel generates a CSV report containing:

### General Statistics

- Total Requests
- Average Response Time

### Top Clients

- IP Address
- Request Count

### Top Resources

- Resource Path
- Request Count

### HTTP Status Distribution

- Status Code
- Count

---

## Security Monitoring

LogSentinel helps identify potentially suspicious behavior by highlighting:

- Excessive requests from a single IP
- Large numbers of HTTP 403 responses
- Large numbers of HTTP 404 responses
- High-frequency access patterns

This makes it useful for studying:

- Web traffic patterns
- Reconnaissance attempts
- Brute-force indicators
- Log analysis workflows

---

## Why LogSentinel?

Many beginner log analyzers load the entire file into memory before processing. LogSentinel uses a streaming approach:

```python
for line in logfile:
    process(line)
```

This allows efficient processing of large log files while keeping memory usage under control.

---

## Technologies

- Python 3
- Regular Expressions (Regex)
- CSV
- Collections
- Argparse

---

## Future Improvements

- GZIP support
- Multi-threaded analysis
- JSON export
- Rich terminal interface
- Interactive dashboard
- Geo-IP enrichment
- Threat intelligence integration

---

## Author

**Mr_Skypunch**

Cybersecurity & AI Student

---

## License

This project is released under the MIT License.
