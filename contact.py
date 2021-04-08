import pyperclip


class Contact:
    contact_list = []  # Created an empty contact list

    def __init__(self, first_name, last_name, phone_number, email):  # Creating new instances of our class
        self.firstName = first_name
        self.lastName = last_name
        self.phoneNumber = phone_number
        self.email = email

    def save_contact(self):
        Contact.contact_list.append(self)

    def delete_contact(self):
        Contact.contact_list.remove(self)

    @classmethod
    def find_by_number(cls, number):
        """
        Method that takes in a number and returns a contact that matches the number
        """
        for contact in cls.contact_list:
            if contact.phoneNumber == number:
                return contact

    @classmethod
    def contact_exists(cls, number):
        """
        Method that takes in a number and confirms if it exists in the contact list
        """
        for contact in cls.contact_list:
            if contact.phoneNumber == number:
                return True

        return False

    @classmethod
    def display_contacts(cls):
        """
        Method that returns the contact list
        """
        return cls.contact_list

    @classmethod
    def copy_email(cls, number):
        contact_found = Contact.find_by_number(number)
        pyperclip.copy(contact_found.email)
