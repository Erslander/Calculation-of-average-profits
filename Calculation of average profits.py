def compute_average(values):
    return sum(values) / len(values)

profits = []
year = 1

while True:
    entry = input(f"Enter profits for year {year} (Press Enter to exit): ").strip()
    if entry == "":
        break
    profits.append(float(entry))
    year += 1

if len(profits) > 0:
    avg = compute_average(profits)
    print(f"Average profits: {avg:.2f}")
else:
    print("No data provided.")
