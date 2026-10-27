import json
import os
import uuid
from dotenv import load_dotenv
from ai_helper import get_ai_suggestion

load_dotenv()


def create_ticket():
    title = input("Enter ticket title: ").strip()

    if not title:
        print("Title cannot be empty.")
        return

    description = input("Enter ticket description: ").strip()

    if not description:
        print("Description cannot be empty.")
        return

    tickets = []

    if os.path.exists("tickets.json"):
        try:
            with open("tickets.json", "r") as file:
                tickets = json.load(file)

            if not isinstance(tickets, list):
                print("Error: tickets.json must contain a list.")
                return

        except (json.JSONDecodeError, OSError):
            print("Could not read tickets.json.")
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

        print("\nTicket created successfully!")
        print("Ticket ID:", ticket["id"])

    except OSError:
        print("Could not save ticket.")
        return

    print("\nGetting AI troubleshooting suggestions...")
    suggestion = get_ai_suggestion(title, description)

    print("\n===== AI SUGGESTION =====")
    print(suggestion)
    print("=========================")


def main():
    while True:
        print("\n===== CAMPUSFLOW TICKET ASSISTANT =====")
        print("1. Create Ticket")
        print("2. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            create_ticket()
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()