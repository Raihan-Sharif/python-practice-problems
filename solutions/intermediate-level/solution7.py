import re
from collections import Counter


def parse_log_file(file_path):
    ips = []
    with open(file_path, 'r') as file:
        for line in file:
            match = re.match(r'(\d+\.\d+\.\d+\.\d+)', line)
            if match:
                ips.append(match.group(1))
    return ips

def count_top_ips(ips, n=3):
    return Counter(ips).most_common(n)

def main():
    # Create a dummy log file
    dummy_log = """192.168.1.1 - - [01/Feb/2023:12:00:00 +0000] "GET /index.html HTTP/1.1" 200 2326
192.168.1.2 - - [01/Feb/2023:12:00:01 +0000] "GET /about.html HTTP/1.1" 200 1234
192.168.1.1 - - [01/Feb/2023:12:00:02 +0000] "POST /login HTTP/1.1" 200 532
192.168.1.3 - - [01/Feb/2023:12:00:03 +0000] "GET /contact.html HTTP/1.1" 404 321
192.168.1.2 - - [01/Feb/2023:12:00:04 +0000] "GET /index.html HTTP/1.1" 200 2326
192.168.1.1 - - [01/Feb/2023:12:00:05 +0000] "GET /home HTTP/1.1" 200 1111
"""
    log_file_path = 'dummy_access.log'
    with open(log_file_path, 'w') as f:
        f.write(dummy_log)

    ips = parse_log_file(log_file_path)
    top_ips = count_top_ips(ips)
    print("Top 3 IPs with the most requests:")
    for ip, count in top_ips:
        print(f"{ip}: {count} requests")

if __name__ == "__main__":
    main()
