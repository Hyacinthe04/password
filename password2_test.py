import unittest # Importing the unittest module
from password2 import Credential # Importing the contact class

class TestCredential(unittest.TestCase):

    '''
    Test class that defines test cases for the contact class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
     # Items up here .......

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credential =  Credential("instagram","hyacinthe","0123") # create contact object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credential.account,"instagram")
        self.assertEqual(self.new_credential.username,"hyacinthe")
        self.assertEqual(self.new_credential.password,"0123")
    
        
    def test_save_credential(self):
        '''
        test_save_contact test case to test if the contact object is saved into
         the contact list
        '''
        self.new_credential.save_credential() # saving the new contact
        self.assertEqual(len(Credential.credential_list),1)
    # Items up here...
    # setup and class creation up here
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Credential.credential_list = []

# other test cases here

    def test_save_multiple_credential(self):
            '''
            test_save_multiple_contact to check if we can save multiple contact
            objects to our contact_list
            '''
            self.new_credential.save_credential()
            test_credential = Credential("instagram","hyacinthe","0123") # new contact
            test_credential.save_credential()
            self.assertEqual(len(Credential.credential_list),2)
# More tests above
    def test_delete_credential(self):
            '''
            test_delete_contact to test if we can remove a contact from our contact list
            '''
            self.new_credential.save_credential()
            test_credential = Credential("instagram","hyacinthe","0123") # new contact
            test_credential.save_credential()

            self.new_credential.delete_credential()# Deleting a contact object
            self.assertEqual(len(Credential.credential_list),1)


    def test_credential_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the contact.
        '''

        self.new_credential.save_credential()
        test_credential =Credential("instagram","hyacinthe","0123") # new contact
        test_credential.save_credential()

        credential_exists = Credential.credential_exist("hyacinthe")

        self.assertTrue(credential_exists)

    def test_display_all_credential(self):
        '''
        method that returns a list of all credentials saved
        '''

        self.assertEqual(Credential.display_credentials(),Credential.credential_list)
    
    def test_find_credential_by_username(self):
        '''
        test to check if we can find a credential by username and display information
        '''

        self.new_credential.save_credential()
        test_credential = Credential("account","username","0123") # new credential 
        test_credential.save_credential()

        found_credential = Credential.find_by_username("hyacinthe")

        self.assertEqual(found_credential.password,test_credential.password)

if __name__ == '__main__':
    unittest.main()
