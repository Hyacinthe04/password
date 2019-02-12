class Credential:
    """
    Class that generates new instances of contacts.
    """

    credential_list = [] # Empty user list

    def __init__(self,account,username,password):

      # docstring removed for simplicity
        self.account = account
        self.username = username
        self.password = password
        
        user_list = [] # Empty contact list
      # Init method up here
    credential_list = [] # Empty contact list
      # Init method up here
    def save_credential(self):

        '''
        save_credential method saves contact objects into contact_list
        '''

        Credential.credential_list.append(self)
    def delete_credential(self):

        '''
        delete_contact method deletes a saved contact from the contact_list
        '''

        Credential.credential_list.remove(self) 

    @classmethod
    def credential_exist(cls,username):

        '''
        Method that checks if a contact exists from the contact list.
        Args:
            number: Phone number to search if it exists
        Returns :
            Boolean: True or false depending if the contact exists
        '''
        for credential in cls.credential_list:
            if credential.username == username:
                    return True

        return False

    @classmethod
    def display_credentials(cls):
        '''
        method that returns the contact list
        '''
        return cls.credential_list