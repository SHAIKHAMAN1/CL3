from collections import Counter

with open(r"C:\Users\DELL\OneDrive\Desktop\CL-3-main\CL-3-main\pract3\input.txt", "r") as f:
    text = f.read().lower()


# Mapper phase
print("MAPPER OUTPUT")
print("=" * 30)
mapped = []
for char in text:
    if char.strip() != "":
        print(f"{char}\t1")
        mapped.append(char)

# Reducer phase
print("\nREDUCER OUTPUT (Final Count)")
print("=" * 30)
char_count = Counter(mapped)
for char, count in sorted(char_count.items()):
    print(f"{char}\t{count}")