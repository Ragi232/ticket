import json
import os
import uuid

def create_ticket():
    title = input("Enter ticket title: ").strip()
    if title == "":
        print("Title cannot be empty")
        return

    description = input("Enter ticket description: ").strip()
    if description == "":
        print("Description cannot be empty")
        return

    tickets = []

    if os.path.exists("tickets.json"):
        try:
            with open("tickets.json", "r") as file:
                tickets = json.load(file)
        except (json.JSONDecodeError, OSError):
            print("Could not read tickets.json")
            return

    ticket = {
        "id": str(uuid.uuid4()),
        "title": title,
        "description": description
    }

    tickets.append(ticket)

    try:
        with open("tickets.json", "w") as file:
            json.dump(tickets, file, indent=4)

        print("Ticket created successfully!")
        print("Ticket ID:", ticket["id"])

    except OSError:
        print("Could not save ticket")


while True:
    print("\n1. Create Ticket")
    print("2. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        create_ticket()
    elif choice == "2":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")