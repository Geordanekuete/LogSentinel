import argparse

from banner import BANNER
from parser import parse_file
from analyzer import LogAnalyzer
from report import export_csv


def main():

    print(BANNER)

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "logfile",
        help="Path to log file"
    )

    args = parser.parse_args()

    analyzer = LogAnalyzer()

    for entry in parse_file(args.logfile):
        analyzer.process(entry)

    print("=" * 50)

    print(
        f"Total Requests : {analyzer.total_requests}"
    )

    print(
        f"Average Response Time : "
        f"{analyzer.get_average_response_time()} ms"
    )

    print("\nTop Clients")

    for ip, count in analyzer.ip_counter.most_common(5):
        print(f"{ip:<20} {count}")

    output = export_csv(analyzer)

    print(f"\nReport saved : {output}")


if __name__ == "__main__":
    main()