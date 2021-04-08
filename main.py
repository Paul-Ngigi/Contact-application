#!/usr/bin/env python3.6

from contact import Contact


def create_contact(fname, lname, phone, email):
    """
    function to create a new name
    """
    new_contact = Contact(fname, lname, phone, email)
    return new_contact


def save_contact(contact):
    """
    function to save contacts
    """
    contact.save_contact()


def delete_contact(contact):
    """
    function to delete a contact
    """
    contact.delete_contact()


def find_contact(number):
    """
    function to find a number
    """
    return Contact.find_by_number(number)


def check_existing_contacts(number):
    """
    Functions that finds a contact by number and returns the contact
    """
    return Contact.find_by_number(number)


def display_contact():
    """
    function to that returns all saved contacts
    """
    return Contact.display_contacts()


def main():
    print("Hello, welcome to your contact list. What is your name?")
    user_name = input()

    print(f"Hello {user_name}. What would you like to do?")
    print("\n")

    while True:
        print("Use these short codes : cc - create a new contact, dc - display contacts, fc - find a new contact,"
              "ex - exit the contact list")

        short_code = input().lower()

        if short_code == 'cc':
            print("New Contact")
            print("-" * 10)

            print("First Name ...")
            f_name = input()

            print("Last Name ...")
            l_name = input()

            print("Phone Number ...")
            p_number = int(input())

            print("Email Address ...")
            e_address = input()

            save_contact(create_contact(f_name, l_name, p_number, e_address))  # Create and save a new contact
            print("\n")
            print(f"New Contact {f_name} {l_name} created")
            print("\n")

        elif short_code == "dc":

            if display_contact():
                print("Here is a list of all your contacts")
                print("\n")

                for contact in display_contact():
                    print(f"{contact.firstName} {contact.lastName} ... {contact.phoneNumber}")

                    print("\n")

            else:
                print("\n")
                print("You don't seem to have any contacts saved yet")
                print("\n")

        elif short_code == "fc":
            print("Enter the number you want to search for")

            search_number = int(input())
            if check_existing_contacts(search_number):
                search_contact = find_contact(search_number)
                print(f"{search_contact.firstName} {search_contact.lastName}")
                print('-' * 20)

                print(f"Phone number ... {search_contact.phoneNumber}")
                print(f"Email Address ... {search_contact.email}")

            else:

                print("This contact doe not exist")

        elif short_code == "ex":
            print("Bye ...")
            break

        else:
            print("I really didn't get that. Please use the short codes")


if __name__ == '__main__':
    main()
