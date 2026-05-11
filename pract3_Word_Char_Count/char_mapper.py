import sys

for line in sys.stdin:
    line = line.strip()
    for char in line:
        if char.strip() != "":
            print(f"{char.lower()}\t1")