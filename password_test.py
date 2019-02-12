import unittest # Importing the unittest module
from password import User # Importing the user class

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

# Items up here 

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("hyacinthe","0123") # create user object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.username,"hyacinthe")
        self.assertEqual(self.new_user.password,"0123")
        




    def test_save_user(self):
        '''
        test_save_contact test case to test if the contact object is saved into
         the contact list
        '''
        self.new_user.save_user() # saving the new contact
        self.assertEqual(len(User.user_list),1)


# setup and class creation up here
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.user_list = []

# other test cases here
    def test_save_multiple_user(self):
            '''
            test_save_multiple_contact to check if we can save multiple contact
            objects to our contact_list
            '''
            self.new_user.save_user()
            test_user = User("username","password") # new contact
            test_user.save_user()
            self.assertEqual(len(User.user_list),2)


# More tests above
    def test_delete_user(self):
            '''
            test_delete_user to test if we can remove a contact from our contact list
            '''
            self.new_user.save_user()
            test_user = User("username","password",) # new contact
            test_user.save_user()

            self.new_user.delete_user()# Deleting a contact object
            self.assertEqual(len(User.user_list),1)
               

    def test_user_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the contact.
        '''

        self.new_user.save_user()
        test_user =User("Test","instagram","hyacinthe","0123") # new contact
        test_user.save_user()

        user_exists = User.user_exist("hyacinthe")

        self.assertTrue(user_exists)
    def test_display_all_user(self):
        '''
        method that returns a list of all contacts saved
        '''

        self.assertEqual(User.display_users(),User.user_list)

    if __name__ == '__main__':
       unittest.main()
    