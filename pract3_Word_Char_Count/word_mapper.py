import sys

for line in sys.stdin:
    line = line.strip()
    for word in line.split():
        print(f"{word.lower()}\t1")