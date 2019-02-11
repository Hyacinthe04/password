import unittest # Importing the unittest module
from password2 import Credentials # Importing the user class

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