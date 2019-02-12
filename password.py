class User:
    """
    Class that generates new instances of contacts.
    """

    user_list = [] # Empty user list

    def __init__(self,username,password):

      # docstring removed for simplicity

        self.username = username
        self.password = password
        
        user_list = [] # Empty contact list
 # Init method up here
    def save_user(self):

        '''
        save_user method saves contact objects into contact_list
        '''

        User.user_list.append(self)

    def delete_user(self):

        '''
        delete_contact method deletes a saved contact from the contact_list
        '''

        User.user_list.remove(self)    

    @classmethod
    def user_exist(cls,username):

        '''
        Method that checks if a contact exists from the contact list.
        Args:
            number: Phone number to search if it exists
        Returns :
            Boolean: True or false depending if the contact exists
        '''
        for user in cls.user_list:

    @classmethod
    def display_users(cls):
        '''
        method that returns the contact list
        '''
        return cls.user_list
 
   
