#!/usr/bin/env python3

import sys

year_data = {}

# Read mapper output
for line in sys.stdin:

    line = line.strip()

    try:
        year, temp = line.split("\t")

        temp = float(temp)

        if year not in year_data:
            year_data[year] = []

        year_data[year].append(temp)

    except:
        continue

# Check if empty
if len(year_data) == 0:

    print("No valid data found.")

    sys.exit()

# Calculate averages
avg_temp = {}

for year in year_data:

    avg_temp[year] = (
        sum(year_data[year]) / len(year_data[year])
    )

# Print yearly averages
print("\n===== Average Temperature Per Year =====")

for year in sorted(avg_temp):

    print(
        f"{year} --> "
        f"{avg_temp[year]:.2f} °C"
    )

# Find coolest and hottest
coolest_year = min(avg_temp, key=avg_temp.get)

hottest_year = max(avg_temp, key=avg_temp.get)

print("\n===== FINAL RESULT =====")

print(
    f"Coolest Year: {coolest_year} "
    f"({avg_temp[coolest_year]:.2f} °C)"
)

print(
    f"Hottest Year: {hottest_year} "
    f"({avg_temp[hottest_year]:.2f} °C)"
)


# type weather_data.csv | python mapper.py | python reducer.py