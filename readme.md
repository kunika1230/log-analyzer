Log File Analyzer (Python Automation Project)

Overview

This project is a Python-based automation tool designed to parse and analyze log files. It extracts error patterns, analyzes system activity, and generates summary reports to reduce manual monitoring effort.

---

Features

* Parses real-world log files (Apache-style logs)
* Extracts status codes (200, 404, 500, etc.)
* Identifies error patterns (4xx, 5xx responses)
* Generates structured summary reports
* Tracks top IP addresses and request frequency
* Automates repetitive log monitoring tasks

---

 Tech Stack

* Python
* File Handling
* Collections (Counter)
* Basic Log Parsing

---

 Project Structure

```
log-analyzer/
│
├── logs/
│   └── app.log
│
├── src/
│   └── log_analyzer.py
│
├── output/
│   └── report.txt
│
├── .gitignore
└── README.md
```

---

How to Run

### 1. Clone the repository

```
git clone https://github.com/yourusername/log-analyzer.git
cd log-analyzer
```

2. Run the script

```
cd src
python log_analyzer.py
```

---

Sample Output

```
===== LOG ANALYSIS REPORT =====

Errors: 3
Success: 4

Top Status Codes:
200 -> 4
500 -> 2
404 -> 1

Top IPs:
192.168.1.1 -> 3
127.0.0.1 -> 2
```

---

 Use Cases

* System log monitoring
* Error tracking and debugging
* Infrastructure health checks
* Automation of repetitive log analysis tasks

---

 Future Enhancements

* Real-time log monitoring
* Email alerts for critical errors
* Dashboard visualization (Streamlit)
* Cloud integration (AWS S3, Lambda)

---

Author

Kunika Auti
