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
        

if __name__ == '__main__':
    unittest.main()