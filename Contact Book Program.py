contact_book = {}
def show_menu():
    print("\nContact Book")
    print("=============")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contact_book[name] = {
        'phone': phone,
        'email': email,
        'address': address
    }
    print(f"Contact for {name} added successfully.")
def view_contacts():
    if not contact_book:
        print("No contacts available.")
    else:
        print("\nContact List:")
        for name, details in contact_book.items():
            print(f"Name: {name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}")
            print(f"Address: {details['address']}")
            print("-" * 20)
def search_contact():
    search_term = input("Enter name or phone number to search: ")
    found = False
    for name, details in contact_book.items():
        if search_term.lower() in name.lower() or search_term in details['phone']:
            print(f"\nContact found:")
            print(f"Name: {name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}")
            print(f"Address: {details['address']}")
            found = True
            break
    if not found:
        print("Contact not found.")
def update_contact():
    name = input("Enter the name of the contact to update: ")
    if name in contact_book:
        phone = input(f"Enter new phone number for {name} (current: {contact_book[name]['phone']}): ")
        email = input(f"Enter new email for {name} (current: {contact_book[name]['email']}): ")
        address = input(f"Enter new address for {name} (current: {contact_book[name]['address']}): ")
        contact_book[name] = {
            'phone': phone,
            'email': email,
            'address': address
        }
        print(f"Contact for {name} updated successfully.")
    else:
        print("Contact not found.")
def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    if name in contact_book:
        del contact_book[name]
        print(f"Contact for {name} deleted successfully.")
    else:
        print("Contact not found.")
def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting the Contact Book.")
            break
        else:
            print("Invalid choice, please try again.")
main()
