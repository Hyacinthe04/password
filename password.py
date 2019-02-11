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

    # @classmethod
    # def find_by_username(cls,username):
    #     '''
    #     Method that takes in a number and returns a contact that matches that number.

    #     Args:
    #         number: Phone number to search for
    #     Returns :
    #         Contact of person that matches the number.
    #     '''

    #     for username in cls.username_list:
    #         if user.username == password:
    #             return user


 
   
