import json


def load_contacts():
    try:
        with open("contacts.json", "r") as file:
            contacts = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        contacts = {}
    return contacts


def save_contacts(contacts):
    with open("contacts.json", "w") as file:
        json.dump(contacts, file, indent=2)



def add_contact(contacts, name, phone, email, age, address):
    if name.strip() == "":
        print("Error: Name cannot be empty.")
        return

    if name in contacts:
        print("Error: Contact with this name already exists.")
        return

    if not phone.isdigit() or len(str(phone)) != 10:
        print("Error: Phone number should contain only digits. and 10 digits only")
        return

    contacts[name] = {"Phone": phone, "Email": email, "age": age, "address": address}
    save_contacts(contacts)
    print(f"Contact '{name}' added successfully!")




def search_contact(contacts, name):
    if name in contacts:
        print(f"Contact Details for '{name}':")
        print(f"Contact found - {name}")
        print(f"Phone: {contacts[name]['Phone']}")
        print(f"Email: {contacts[name]['Email']}")
        print(f"age: {contacts[name]['age']}")
        print(f"address: {contacts[name]['address']}")
    else:
        print(f"Contact '{name}' not found!")


def update_contact(contacts):
    name = input("Enter contact name to update: ")
    if name not in contacts:
        print(f"Contact '{name}' not found. Use add option to create a new contact.")
        return

    new_name = input("Enter new contact name (press Enter to keep the current name): ")
    new_phone = input("Enter new contact phone number (press Enter to keep the current phone number): ")
    new_email = input("Enter new contact email (press Enter to keep the current email): ")
    new_age = input("Enter new contact age(press Enter to keep the current age): ")
    new_address = input("Enter new contact address(press Enter to keep the current address): ")

    if new_name.strip() != "":
        contacts[new_name] = contacts.pop(name)
        name = new_name

    if new_phone.strip() != "":
        if not new_phone.isdigit() or len(new_phone) != 10:
            print("Invalid phone number. Please enter a 10-digit number.")
            return
        contacts[name]["phone"] = new_phone

    if new_email.strip() != "":
        contacts[name]["Email"] = new_email

    if new_age.strip() != "":
        contacts[name]['age'] = new_age

    if new_address.strip() !="":
        contacts[name]["address"] = new_address

    save_contacts(contacts)
    print(f"Contact '{name}' updated successfully.")


def main():
    contacts = load_contacts()

    while True:
        print("\nContact Management System Menu:")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            name = input("Enter contact name: ")
            phone = input("Enter contact phone number: ")
            while phone=='':
                if phone!='':
                    continue
                else:
                    phone = input(" plzz enter phone number :")

            email = input("Enter contact email address: ")
            while email=='':
                if email!='':
                    continue
                else:
                    email = input(" plzz enter email address :")
            age = input("Enter contact age: ")
            while age=='':
                if age!='':
                    continue
                else:
                    age = input(" plzz enter age :")
            address = input("Enter contact address: ")
            while address=='':
                if address!='':
                    continue
                else:
                    address = input(" plzz enter complete address :")
            add_contact(contacts, name, phone, email,age,address)
        elif choice == "2":
            name = input("Enter contact name to search: ")
            search_contact(contacts, name)
        elif choice == "3":
            update_contact(contacts)
        elif choice == "4":
            save_contacts(contacts)
            print("Exiting Contact Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option (1/2/3/4).")


if __name__ == "__main__":
    main()

