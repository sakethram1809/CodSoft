class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self):
        name = input("Enter contact name: ")
        phone = input("Enter contact phone number: ")
        email = input("Enter contact email: ")
        address = input("Enter contact address: ")

        self.contacts[name] = {"phone": phone, "email": email, "address": address}

        print(f"Contact {name} added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("Contact list is empty.")
        else:
            print("Contact List:")
            for name, details in self.contacts.items():
                print(f"Name: {name}, Phone: {details['phone']}")

    def search_contact(self):
        search_term = input("Enter name or phone number to search: ")

        for name, details in self.contacts.items():
            if search_term in [name, details["phone"]]:
                print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}, Address: {details['address']}")
                return

        print("Contact not found.")

    def update_contact(self):
        name = input("Enter contact name to update: ")

        if name in self.contacts:
            phone = input("Enter new phone number: ")
            email = input("Enter new email: ")
            address = input("Enter new address: ")

            self.contacts[name] = {"phone": phone, "email": email, "address": address}

            print(f"Contact {name} updated successfully!")
        else:
            print("Contact not found.")

    def delete_contact(self):
        name = input("Enter contact name to delete: ")

        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact {name} deleted successfully!")
        else:
            print("Contact not found.")

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            contact_book.add_contact()
        elif choice == "2":
            contact_book.view_contacts()
        elif choice == "3":
            contact_book.search_contact()
        elif choice == "4":
            contact_book.update_contact()
        elif choice == "5":
            contact_book.delete_contact()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()