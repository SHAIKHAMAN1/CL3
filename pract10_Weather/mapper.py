#!/usr/bin/env python3

import sys

for line in sys.stdin:

    line = line.strip()

    # Skip header
    if line.startswith("year"):
        continue

    try:
        year, temp = line.split(",")

        print(f"{year}\t{temp}")

    except:
        continue