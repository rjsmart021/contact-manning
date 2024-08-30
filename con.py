import re
import json

# Function to display menu
def display_menu():
    print("Welcome to the Contact Management System!")
    print("Menu:")
    print("1. Add a new contact")
    print("2. Edit an existing contact")
    print("3. Delete a contact")
    print("4. Search for a contact")
    print("5. Display all contacts")
    print("6. Export contacts to a text file")
    print("7. Import contacts from a text file")
    print("8. Quit")

# Function to add a new contact
def add_contact(contacts):
    print("\nAdding a new contact:")
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    additional_info = input("Enter additional information (optional): ")
    contact = {"Name": name, "Phone": phone, "Email": email, "Additional Info": additional_info}
    contacts[email] = contact
    print("Contact added successfully!")

# Function to edit an existing contact
def edit_contact(contacts):
    print("\nEditing an existing contact:")
    email = input("Enter the email of the contact you want to edit: ")
    if email in contacts:
        print("Existing details:")
        print(contacts[email])
        name = input("Enter new name: ")
        phone = input("Enter new phone number: ")
        additional_info = input("Enter new additional information: ")
        contacts[email]["Name"] = name
        contacts[email]["Phone"] = phone
        contacts[email]["Additional Info"] = additional_info
        print("Contact edited successfully!")
    else:
        print("Contact not found.")

# Function to delete a contact
def delete_contact(contacts):
    print("\nDeleting a contact:")
    email = input("Enter the email of the contact you want to delete: ")
    if email in contacts:
        del contacts[email]
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")

# Function to search for a contact
def search_contact(contacts):
    print("\nSearching for a contact:")
    email = input("Enter the email of the contact you want to search for: ")
    if email in contacts:
        print("Contact details:")
        print(contacts[email])
    else:
        print("Contact not found.")

# Function to display all contacts
def display_all_contacts(contacts):
    print("\nAll contacts:")
    for email, contact in contacts.items():
        print("Email:", email)
        print("Details:", contact)
        print()

# Function to export contacts to a text file
def export_contacts(contacts):
    print("\nExporting contacts to a text file:")
    with open("contacts.txt", "w") as file:
        json.dump(contacts, file)
    print("Contacts exported successfully!")

# Function to import contacts from a text file
def import_contacts(contacts):
    print("\nImporting contacts from a text file:")
    try:
        with open("contacts.txt", "r") as file:
            contacts.update(json.load(file))
        print("Contacts imported successfully!")
    except FileNotFoundError:
        print("No contacts file found.")
    except Exception as e:
        print("Error occurred while importing contacts:", e)

# Function to validate email format
def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)

# Main function
def main():
    contacts = {}
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            edit_contact(contacts)
        elif choice == "3":
            delete_contact(contacts)
        elif choice == "4":
            search_contact(contacts)
        elif choice == "5":
            display_all_contacts(contacts)
        elif choice == "6":
            export_contacts(contacts)
        elif choice == "7":
            import_contacts(contacts)
        elif choice == "8":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 8.")

if __name__ == "__main__":
    main()
