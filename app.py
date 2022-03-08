from database import add_entry, view_entries

menu = """
-------------------------------------------------------

Please select one of the following options:
1) Add new entry for today.
2) View entries.
3) Exit.

Your selection: \n"""

welcome = """
Welcome to the programming diary! """

print(welcome)

while ( user_input := input(menu)) != "3":
    if user_input == "1":
        add_entry()
    elif user_input == "2":
        view_entries()
    else:
        print("\n Invalid option, please try again! \n")
