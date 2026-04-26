import os
import re
from collections import Counter
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

log_file = os.path.join("..", "logs", "app.log")

error_count = 0
success_count = 0

status_counter = Counter()
ip_counter = Counter()
endpoint_counter = Counter()
error_counter = Counter()

pattern = r'(\d+\.\d+\.\d+\.\d+).*?"\w+\s(.*?)\sHTTP.*?"\s(\d{3})'

with open(log_file, "r", encoding="utf-8", errors="ignore") as file:
    for line in file:
        match = re.search(pattern, line)
        if not match:
            continue

        ip = match.group(1)
        endpoint = match.group(2)
        status = match.group(3)

        ip_counter[ip] += 1
        status_counter[status] += 1
        endpoint_counter[endpoint] += 1

        if status.startswith("4") or status.startswith("5"):
            error_count += 1
            error_counter[status] += 1
        elif status.startswith("2"):
            success_count += 1

# ================= PDF =================

pdf_path = os.path.join("..", "output", "final_report.pdf")

with PdfPages(pdf_path) as pdf:

    # PAGE 1
    fig = plt.figure(figsize=(8,6))
    plt.axis('off')

# ===== INSIGHTS =====
    error_rate = round((error_count / (error_count + success_count)) * 100, 2)

    insight = f"""
    LOG ANALYSIS REPORT

    SYSTEM HEALTH:
    - Total Requests: {error_count + success_count}
    - Success Requests: {success_count}
    - Failed Requests: {error_count}
    - Error Rate: {error_rate}%

    INTERPRETATION:
    """

    # Add interpretation logic
    if error_rate < 5:
        insight += "- System is stable and performing well.\n"
    elif error_rate < 15:
        insight += "- Moderate errors detected. Needs monitoring.\n"
    else:
        insight += "- High error rate! Immediate attention required.\n"

    # Add specific insights
    if error_counter.get("404", 0) > 100:
        insight += "- Many 404 errors → Broken links or missing pages.\n"

    if error_counter.get("500", 0) > 0:
        insight += "- Server errors detected → Backend issue.\n"

    if max(ip_counter.values()) > 300:
        insight += "- High traffic from single IP → Possible bot.\n"

    insight += f"""

    TOP FINDINGS:
    - Most common status: {status_counter.most_common(1)}
    - Most active IP: {ip_counter.most_common(1)}
    - Most used endpoint: {endpoint_counter.most_common(1)}
    """

    plt.text(0.05, 0.5, insight, fontsize=10)
    pdf.savefig(fig)
    plt.close(fig)

    # PAGE 2
    fig = plt.figure()
    plt.bar(list(status_counter.keys()), list(status_counter.values()))
    plt.title("Status Code Distribution\n200=Success, 4xx/5xx=Errors")
    pdf.savefig(fig)
    plt.close(fig)

    # PAGE 3
    top_ips = ip_counter.most_common(5)
    ips = [i for i,_ in top_ips]
    counts = [c for _,c in top_ips]

    fig = plt.figure()
    plt.bar(ips, counts)
    plt.title("Top IPs (High traffic = heavy user/bot)")
    pdf.savefig(fig)
    plt.close(fig)

    # PAGE 4
    top_ep = endpoint_counter.most_common(5)
    ep = [e for e,_ in top_ep]
    cnt = [c for _,c in top_ep]

    fig = plt.figure()
    plt.bar(ep, cnt)
    plt.xticks(rotation=30)
    plt.title("Top Endpoints (Most used features)")
    pdf.savefig(fig)
    plt.close(fig)

print("PDF WORKING ✅")