import re

def extract_ips(filename):
    result = []

    with open(filename) as f:
        for line in f:
            result += re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', line)

    return result

print(extract_ips("demo.txt"))
