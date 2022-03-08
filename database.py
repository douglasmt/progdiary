entries = []

def add_entry():
    entry_content =  input("\nWhat have you learned today? ")
    entry_date =  input("Enter the date: ")

    entries.append({"content" : entry_content, "date": entry_date })

def view_entries():
    print(f"\n --- Your agenda ---")
    for entry in entries:
        print(f"{entry['date']} \n{entry['content']}\n")