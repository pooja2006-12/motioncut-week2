import json
from datetime import datetime, timedelta

DATA_FILE = "festivals.json"

# ---------- Helpers ----------
def load_festivals():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def save_festivals(festivals):
    with open(DATA_FILE, "w") as f:
        json.dump(festivals, f, indent=4)

def parse_date(date_str):
    formats = ["%Y-%m-%d", "%d-%m-%Y", "%Y/%m/%d", "%d/%m/%Y"]
    for fmt in formats:
        try:
            return datetime.strptime(date_str, fmt).date()
        except ValueError:
            pass
    return None

# ---------- Core Features ----------
def add_festival():
    name = input("Enter festival name: ").strip()
    date_str = input("Enter date (YYYY-MM-DD or DD-MM-YYYY): ").strip()
    date = parse_date(date_str)
    if not date:
        print("Invalid date format!")
        return
    note = input("Enter optional note: ").strip()
    festivals = load_festivals()
    festivals.append({"name": name, "date": date.strftime("%Y-%m-%d"), "note": note})
    festivals.sort(key=lambda x: x["date"])
    save_festivals(festivals)
    print(f"Festival '{name}' added!")

def view_festivals():
    festivals = load_festivals()
    if not festivals:
        print("No festivals saved yet.")
        return
    print("\nSaved Festivals:")
    for i, f in enumerate(festivals, 1):
        print(f"{i}. {f['name']} on {f['date']} ({f.get('note','')})")

def delete_festival():
    festivals = load_festivals()
    view_festivals()
    if not festivals:
        return
    try:
        idx = int(input("Enter number to delete: "))
        removed = festivals.pop(idx-1)
        save_festivals(festivals)
        print(f"Removed {removed['name']}.")
    except (ValueError, IndexError):
        print("Invalid selection.")

def check_reminders():
    today = datetime.today().date()
    upcoming = load_festivals()
    for f in upcoming:
        f_date = parse_date(f['date'])
        if not f_date: continue
        days_left = (f_date - today).days
        if days_left == 0:
            print(f"🎉 TODAY: {f['name']}! {f.get('note','')}")
        elif 0 < days_left <= 7:
            print(f"⏳ {f['name']} is in {days_left} days ({f['date']})")

def export_festivals():
    filename = input("Enter export filename (e.g., export.json): ").strip()
    data = load_festivals()
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
    print(f"Festivals exported to {filename}")

def import_festivals():
    filename = input("Enter import filename: ").strip()
    try:
        with open(filename, "r") as f:
            data = json.load(f)
        save_festivals(data)
        print("Festivals imported successfully.")
    except Exception as e:
        print("Import failed:", e)

# ---------- Main Loop ----------
def main():
    while True:
        print("\n=== Festival Reminder Bot ===")
        print("1. View all festivals")
        print("2. Add a new festival")
        print("3. Delete a festival")
        print("4. Check reminders")
        print("5. Export festivals")
        print("6. Import festivals")
        print("7. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            view_festivals()
        elif choice == "2":
            add_festival()
        elif choice == "3":
            delete_festival()
        elif choice == "4":
            check_reminders()
        elif choice == "5":
            export_festivals()
        elif choice == "6":
            import_festivals()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
