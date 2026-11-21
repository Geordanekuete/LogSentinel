import csv
from datetime import datetime


def export_csv(analyzer):

    filename = (
        f"reports/log_report_"
        f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    )

    with open(filename, "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow(["Metric", "Value"])

        writer.writerow(
            ["Total Requests", analyzer.total_requests]
        )

        writer.writerow(
            ["Average Response Time",
             analyzer.get_average_response_time()]
        )

        writer.writerow([])

        writer.writerow(["Top IPs"])

        for ip, count in analyzer.ip_counter.most_common(10):
            writer.writerow([ip, count])

        writer.writerow([])

        writer.writerow(["Top Resources"])

        for resource, count in analyzer.resource_counter.most_common(10):
            writer.writerow([resource, count])

        writer.writerow([])

        writer.writerow(["HTTP Status"])

        for status, count in analyzer.status_counter.items():
            writer.writerow([status, count])

    return filename