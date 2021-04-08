import unittest
import pyperclip
from contact import Contact


class TestContact(unittest.TestCase):
    def setUp(self) -> None:
        """
        set up method to run before each test case
        """
        self.new_contact = Contact("Paul", "Ngigi", "0714060467", "paulkush7777@gmail.com")

    def test_init(self):
        """
        test_init test case to test if the objects are being initialized correctly
        """
        self.assertEqual(self.new_contact.firstName, "Paul")
        self.assertEqual(self.new_contact.lastName, "Ngigi")
        self.assertEqual(self.new_contact.phoneNumber, "0714060467")
        self.assertEqual(self.new_contact.email, "paulkush7777@gmail.com")

    def test_save_contact(self):
        """
        test_save_contact test case tests if the contacts are being saved into the
        contact list
        """
        self.new_contact.save_contact()

        self.assertEqual(len(Contact.contact_list), 1)

    def tearDown(self) -> None:
        """
        The tearDown method helps to clean up after each test case has run
        """
        Contact.contact_list = []

    def test_save_multiple_contacts(self):
        """
        test_save_multiple_contacts test case tests if multiple contacts are added to the
        contact list
        """
        self.new_contact.save_contact()
        test_user = Contact("Test", "User", "0711111111", "test@user.com")
        test_user.save_contact()

        self.assertEqual(len(Contact.contact_list), 2)

    def test_delete_contact(self):
        """
        test_delete_contact test case tests if one can delete a contact from the
        contact list
        """
        self.new_contact.save_contact()
        test_user = Contact("Test", "User", "0711111111", "test@user.com")
        test_user.save_contact()

        test_user.delete_contact()

        self.assertEqual(len(Contact.contact_list), 1)

    def test_find_contact_number(self):
        """
        test_find_contact_number test case tests if one can find a contact by number
        and display its information
        """
        self.new_contact.save_contact()
        test_user = Contact("Test", "User", "0711111111", "test@user.com")
        test_user.save_contact()

        found_contact = Contact.find_by_number("0711111111")

        self.assertEqual(found_contact.email, test_user.email)

    def test_contact_exists(self):
        """
        test_contact_exists test case test if a contact actually exists in the contact list
        """
        self.new_contact.save_contact()
        test_user = Contact("Test", "User", "0711111111", "test@user.com")
        test_user.save_contact()

        contact_exists = Contact.contact_exists("0714060467")

        self.assertTrue(contact_exists)

    def test_display_all_contacts(self):
        """
        test_display_all_contacts test case tests if one can return a list of saved contacts
        """
        self.assertEqual(Contact.display_contacts(), Contact.contact_list)

    def test_copy_email(self):
        """
        Test to confirm we are copying email address from a found contact
        """
        self.new_contact.save_contact()
        Contact.copy_email("0714060467")

        self.assertEqual(self.new_contact.email, pyperclip.paste())


if __name__ == '__main__':
    unittest.main()
