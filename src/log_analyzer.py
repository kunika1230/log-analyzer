import os
from collections import Counter

log_file = os.path.join("..", "logs", "app.log")
output_file = os.path.join("..", "output", "report.txt")

error_count = 0
success_count = 0
status_codes = []
ip_addresses = []

with open(log_file, "r") as file:
    for line in file:
        parts = line.split()

        ip = parts[0]
        status = parts[-1]

        ip_addresses.append(ip)
        status_codes.append(status)

        if status.startswith("5") or status.startswith("4"):
            error_count += 1
        elif status.startswith("2"):
            success_count += 1

top_status = Counter(status_codes)
top_ips = Counter(ip_addresses)

with open(output_file, "w") as report:
    report.write("===== LOG ANALYSIS REPORT =====\n\n")
    report.write(f"Errors: {error_count}\n")
    report.write(f"Success: {success_count}\n\n")

    report.write("Top Status Codes:\n")
    for code, count in top_status.items():
        report.write(f"{code} -> {count}\n")

    report.write("\nTop IPs:\n")
    for ip, count in top_ips.items():
        report.write(f"{ip} -> {count}\n")

print("Report generated successfully!")