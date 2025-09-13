import csv
from pathlib import Path

CSV_PATH = Path("expense_tracker.csv")

def ensure_csv_with_header():
    if not CSV_PATH.exists():
        with CSV_PATH.open("w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Item", "Cost"])

def add_expenses():
    items, costs = [], []
    while True:
        choice = input("Add an item? (y/n): ").strip().lower()
        if choice in ("y", "yes"):
            name = input("Enter item name: ").strip()
            if not name:
                print("Item name cannot be empty.")
                continue
            # validate cost
            try:
                cost = float(input("Enter cost: ").strip())
                if cost < 0:
                    print("Cost cannot be negative.")
                    continue
            except ValueError:
                print("Please enter a valid number for cost.")
                continue
            items.append(name)
            costs.append(cost)
        elif choice in ("n", "no"):
            break
        else:
            print("Please answer y/n.")
    if items:
        with CSV_PATH.open("a", newline="") as f:
            writer = csv.writer(f)
            for name, cost in zip(items, costs):
                writer.writerow([name, cost])
                print(f"Saved: {name}, ${cost:.2f}")
    else:
        print("No items to save.")

def view_report():
    if not CSV_PATH.exists():
        print("No expenses yet. Add some first.")
        return
    total = 0.0
    count = 0
    with CSV_PATH.open("r", newline="") as f:
        reader = csv.reader(f)
        header = next(reader, None)  # skip header if present
        for row in reader:
            if len(row) < 2:
                continue  # skip malformed rows
            product = row[0].strip()
            try:
                cost = float(row[1])
            except ValueError:
                # skip rows with non-numeric cost (from old runs/typos)
                continue
            total += cost
            count += 1
            print(f"{product}: ${cost:.2f}")
    print("--------")
    print(f"Total items: {count}")
    print(f"Total expense: ${total:.2f}")
    if count:
        print(f"Average per item: ${total / count:.2f}")

def main():
    ensure_csv_with_header()
    while True:
        print("\nWhat do you want to do?")
        print("----------------------")
        print("1. Add expenses")
        print("2. View report")
        print("3. Exit")
        selection = input("Choose 1/2/3: ").strip()
        if selection == "1":
            add_expenses()
        elif selection == "2":
            view_report()
        elif selection == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
